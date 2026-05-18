import json
import os
from services.parking_service import ParkingService

class RealParkingService(ParkingService):
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'database.json')

    def _read_database(self) -> dict:
        with open(self.db_path, 'r') as file:
            return json.load(file)

    def _write_database(self, data: dict):
        with open(self.db_path, 'w') as file:
            json.dump(data, file, indent=4)

    def check_availability(self, location: str) -> str:
        data = self._read_database()
        if location in data:
            info = data[location]
            return f"[SYSTEM] {location} - Status: {info['status']}, Occupied: {info['occupied']}/{info['capacity']}"
        return f"[SYSTEM] Location {location} not found."

    def update_status(self, location: str, status: str) -> str:
        data = self._read_database()
        if location in data:
            data[location]['status'] = status
            self._write_database(data)
            return f"[SYSTEM] Status of {location} successfully updated to {status}."
        return f"[SYSTEM] Location {location} not found."

    def download_report(self) -> str:
        return "[SYSTEM] Monthly parking operational report successfully downloaded."
