from vehicle import Vehicle
from vehicle_type import VehicleType


class ParkingSpot():
    
    def __init__(self, spot_num) -> None:
        self.spot_num = spot_num
        self.vehicle = None
        self.vehicle_type = VehicleType.CAR
    
    
    def is_available(self):
        return self.vehicle is None
    
    def park_vehicle(self, vehicle: Vehicle) -> None:
        if self.is_available() and self.vehicle_type == vehicle.get_type():
            self.vehicle = vehicle
        else:
            raise ValueError("Invalid vehicle type or spot already occupied.")
    
    
    def unpark_vehicle(self) -> None:
        self.vehicle = None
        
    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type
    
    def get_vehicle(self) -> Vehicle:
        return self.vehicle
    
    def get_spot_number(self) -> int:
        return self.spot_num