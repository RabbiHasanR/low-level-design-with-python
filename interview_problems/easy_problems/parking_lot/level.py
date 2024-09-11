from parking_spot import ParkingSpot
from vehicle import Vehicle

class Level:
    
    def __init__(self, floor, total_spots) -> None:
        self.floor = floor
        self.total_spots = [ParkingSpot(i) for i in range(total_spots)]
        
    
    
    def get_level(self) -> int:
        return self.floor
    
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.total_spots:
            if spot.is_available() and spot.get_vehicle_type() == vehicle.get_type():
                spot.park_vehicle(vehicle=vehicle)
                return True
        return False
    
    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.total_spots:
            if not spot.is_available() and spot.get_vehicle_type() == vehicle.get_type():
                spot.unpark_vehicle(vehicle)
                return True
        return False
    
    def display_avilability(self) -> None:
        print(f"Level {self.floor} Availability:")
        for spot in self.total_spots:
            print(f"Spot {spot.get_spot_number()}: {"Available" if spot.is_available() else "Occupied"}")
        