from parking_lot import ParkingLot
from level import Level
from car import Car
from truck import Truck
from motorcycle import Motorcycle




class ParkingLotDemo:
    
    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1, 100))
        parking_lot.add_level(Level(2, 80))
        
        car = Car("ABC123")
        truck = Truck("XYZ789")
        motorcycle = Motorcycle("M1234")
        
        
        # park vehicle
        is_car_parked = parking_lot.park_vehicle(car)
        is_truck_parked = parking_lot.park_vehicle(truck)
        is_motorcycle_parked = parking_lot.park_vehicle(motorcycle)
        
        
        print(is_car_parked, is_truck_parked, is_motorcycle_parked)
        
        
        # display availability
        parking_lot.display_availability()
        
        # unpark vehicle
        is_motorcyle_unparked = parking_lot.unpark_vehicle(motorcycle)
        print(is_motorcyle_unparked)
        
        # display updated availability
        parking_lot.display_availability()
        


if __name__ == "__main__":
    ParkingLotDemo.run()