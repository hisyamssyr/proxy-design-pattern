# ParkSpot Proxy - Proxy Design Pattern

Proyek ini adalah contoh implementasi **Proxy Design Pattern** menggunakan bahasa Python. Program mensimulasikan sistem manajemen parkir sederhana (*ParkSpot*) di mana hak akses pengguna dikontrol menggunakan sebuah Proxy sebelum permintaan diteruskan ke layanan utama.

## Deskripsi

Pada aplikasi ini, terdapat dua jenis pengguna (berdasarkan *role*):
1. **Student (Mahasiswa):** Hanya diizinkan untuk melihat ketersediaan parkir.
2. **Parking Attendant (Penjaga Parkir):** Diizinkan untuk melihat ketersediaan parkir, memperbarui status parkir, dan mengunduh laporan.

Proxy bertindak sebagai lapisan keamanan (*Protection Proxy*) yang memverifikasi peran pengguna sebelum memanggil fungsi pada layanan asli (`RealParkingService`).

## Struktur Direktori

```text
parkspot_proxy/
├── data/
│   └── database.json              # Simulasi database penyimpanan status parkir
├── models/
│   ├── __init__.py
│   └── user.py                    # Model data pengguna (User)
├── services/
│   ├── __init__.py
│   ├── parking_service.py         # Interface (Subject)
│   ├── real_parking_service.py    # Logika inti sistem parkir (Real Subject)
│   └── proxy_parking_service.py   # Pengendali akses (Proxy)
└── main.py                        # Entry point untuk simulasi program
```

## Cara Menjalankan

1. Pastikan Anda sudah menginstal Python 3.x.
2. *Clone* repositori ini atau *download source code*.
3. Buka terminal dan arahkan ke direktori proyek (`parkspot_proxy`).
4. Jalankan perintah berikut:

```bash
python main.py
```

## Contoh Output (Simulasi)

Saat program dijalankan, Anda akan melihat bagaimana Proxy secara dinamis memberikan atau menolak akses berdasarkan *role* pengguna:

```text
=== STUDENT ACCESS SIMULATION ===

[Hisyam Syafa Raditya] Requesting access to view availability at Informatics Building...
[SYSTEM] Informatics Building - Status: Closed, Occupied: 80/100

[Hisyam Syafa Raditya] Requesting access to update status of Informatics Building...
[ACCESS DENIED] Hisyam Syafa Raditya does not have permission for this action.

=== PARKING ATTENDANT ACCESS SIMULATION ===

[Bapak Budi] Requesting access to update status of Informatics Building...
[SYSTEM] Status of Informatics Building successfully updated to Closed.

[Bapak Budi] Requesting access to view availability at Informatics Building...
[SYSTEM] Informatics Building - Status: Closed, Occupied: 80/100

[Bapak Budi] Requesting access to download report...
[SYSTEM] Monthly parking operational report successfully downloaded.
```

## Penjelasan Proxy Design Pattern pada Study Case Ini

- **`ParkingService` (Subject Interface):** Sebuah *abstract class* / antarmuka yang mendefinisikan operasi dasar yang tersedia, seperti `check_availability`, `update_status`, dan `download_report`.
- **`RealParkingService` (Real Subject):** Kelas yang berisi logika inti / sebenarnya dari sistem parkir. Kelas ini mengelola interaksi aktual dengan simulasi basis data (`database.json`).
- **`ProxyParkingService` (Proxy):** Mengimplementasikan antarmuka yang sama dengan `Subject`, tetapi menambahkan lapisan validasi hak akses (*Protection Proxy*). Proxy memeriksa *role* dari objek `User` yang meminta akses. Jika memenuhi syarat (misal: hanya Penjaga Parkir yang bisa mengubah status), maka ia meneruskan eksekusinya ke `RealParkingService`; jika tidak, ia akan langsung mengembalikan pesan *Access Denied* tanpa menyentuh *Real Subject*.

## Penjelasan Program per Baris

Berikut adalah rincian fungsionalitas tiap baris kode dari seluruh file program yang digunakan pada aplikasi ini:

### 1. `main.py`
| Baris | Penjelasan |
|---|---|
| 1-2 | Mengimpor modul-modul yang dibutuhkan (`User` dan `ProxyParkingService`). |
| 4 | Memeriksa apakah skrip dijalankan langsung sebagai program utama (bukan diimpor). |
| 5-6 | Membuat instance `User` untuk mensimulasikan peran mahasiswa bernama "Hisyam Syafa Raditya" dan petugas parkir bernama "Bapak Budi". |
| 8-9 | Menginisialisasi `ProxyParkingService` untuk masing-masing objek pengguna (`student` dan `attendant`). |
| 11-13 | Mensimulasikan permintaan akses dari *student* (mahasiswa) lalu mencetak outputnya ke terminal. |
| 15-18 | Mensimulasikan permintaan akses dari *parking attendant* (petugas parkir) lalu mencetak outputnya ke terminal. |

### 2. `models/user.py`
| Baris | Penjelasan |
|---|---|
| 1-4 | Mendefinisikan kelas `User` sebagai representasi pengguna, beserta konstruktor `__init__` untuk menginisialisasi atribut `name` dan `role`. |

### 3. `services/parking_service.py`
| Baris | Penjelasan |
|---|---|
| 1 | Mengimpor kelas `ABC` (Abstract Base Class) dan dekorator `abstractmethod` dari modul bawaan `abc`. |
| 3-6 | Mendefinisikan antarmuka/kelas abstrak `ParkingService` beserta deklarasi antarmuka metode `check_availability`. |
| 8-10 | Deklarasi antarmuka metode `update_status` (wajib diimplementasikan oleh kelas turunan). |
| 12-14 | Deklarasi antarmuka metode `download_report` (wajib diimplementasikan oleh kelas turunan). |

### 4. `services/proxy_parking_service.py`
| Baris | Penjelasan |
|---|---|
| 1-3 | Mengimpor modul-modul yang diperlukan (kelas `User`, antarmuka `ParkingService`, dan layanan aktual `RealParkingService`). |
| 5-8 | Mendefinisikan kelas `ProxyParkingService` serta mengatur inisialisasi objek pengguna dan instansiasi layanan aktual di dalam konstruktor. |
| 10-11 | Membuat fungsi *helper* privat `_check_attendant_access` untuk memeriksa validitas izin otoritas *parking attendant*. |
| 13-15 | Mengimplementasikan metode `check_availability` yang bebas diakses siapapun untuk diteruskan (*delegate*) langsung ke *real service*. |
| 17-21 | Mengimplementasikan metode `update_status` dengan melakukan pengecekan hak akses terlebih dahulu. Jika lolos, eksekusi diteruskan ke *real service*; jika tidak, akses ditolak. |
| 23-27 | Mengimplementasikan metode `download_report` dengan mekanisme perlindungan (*Protection Proxy*) hak akses yang serupa. |

### 5. `services/real_parking_service.py`
| Baris | Penjelasan |
|---|---|
| 1-3 | Mengimpor modul bawaan (`json`, `os`) dan modul antarmuka `ParkingService`. |
| 5-7 | Mendefinisikan kelas `RealParkingService` (Sebagai *Real Subject*) yang mengimplementasikan antarmuka, serta menentukan letak *path* file databasenya. |
| 9-11 | Menyediakan prosedur baca privat `_read_database` untuk mengekstrak dan mem-parsing data file JSON ke dalam objek *dictionary* Python. |
| 13-15 | Menyediakan prosedur tulis privat `_write_database` untuk memperbarui dan menyimpan kembali manipulasi *dictionary* tersebut ke format *file JSON*. |
| 17-22 | Menerapkan fitur `check_availability` yang akan membaca informasi *database*, lalu merespon dengan *string* info ketersediaan atau laporan kegagalan. |
| 24-30 | Menerapkan fitur `update_status` yang menimpa atribut *status* pada data spesifik lalu memanggil ulang operasi tulis untuk disimpan. |
| 32-33 | Menerapkan prosedur `download_report` yang berfungsi sederhana untuk mensimulasikan penyelesaian proses pengunduhan laporan. |
