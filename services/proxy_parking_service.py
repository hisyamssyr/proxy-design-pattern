from models.user import User
from services.parking_service import ParkingService
from services.real_parking_service import RealParkingService

class ProxyParkingService(ParkingService):
    def __init__(self, user: User):
        self._user = user
        self._real_service = RealParkingService()

    def _check_attendant_access(self) -> bool:
        return self._user.role.lower() == 'parking attendant'

    def check_availability(self, location: str) -> str:
        print(f"\n[{self._user.name}] Requesting access to view availability at {location}...")
        return self._real_service.check_availability(location)

    def update_status(self, location: str, status: str) -> str:
        print(f"\n[{self._user.name}] Requesting access to update status of {location}...")
        if self._check_attendant_access():
            return self._real_service.update_status(location, status)
        return f"[ACCESS DENIED] {self._user.name} does not have permission for this action."

    def download_report(self) -> str:
        print(f"\n[{self._user.name}] Requesting access to download report...")
        if self._check_attendant_access():
            return self._real_service.download_report()
        return f"[ACCESS DENIED] {self._user.name} does not have permission for this action."
