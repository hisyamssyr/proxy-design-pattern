from abc import ABC, abstractmethod

class ParkingService(ABC):
    @abstractmethod
    def check_availability(self, location: str) -> str:
        pass

    @abstractmethod
    def update_status(self, location: str, status: str) -> str:
        pass

    @abstractmethod
    def download_report(self) -> str:
        pass
