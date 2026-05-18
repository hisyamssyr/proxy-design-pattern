from models.user import User
from services.proxy_parking_service import ProxyParkingService

if __name__ == "__main__":
    student = User(name="Hisyam Syafa Raditya", role="Student")
    attendant = User(name="Bapak Budi", role="Parking Attendant")

    student_access = ProxyParkingService(student)
    attendant_access = ProxyParkingService(attendant)

    print("=== STUDENT ACCESS SIMULATION ===")
    print(student_access.check_availability("Informatics Building"))
    print(student_access.update_status("Informatics Building", "Closed"))

    print("\n=== PARKING ATTENDANT ACCESS SIMULATION ===")
    print(attendant_access.update_status("Informatics Building", "Closed"))
    print(attendant_access.check_availability("Informatics Building"))
    print(attendant_access.download_report())