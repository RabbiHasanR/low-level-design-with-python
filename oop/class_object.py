class Car:
    __slots__ = ['make', 'model', 'year']
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
    
    
    def start_engine(self):
        return f"{self.year} {self.make} {self.model}'s engine started."
    
    
    

# creating an object
my_car = Car('Toyota', 'Corolla', 2020)
# my_car.name = 'rabbi'

# print(my_car.name)
# print(my_car.__dict__)
print(my_car.__slots__)
print(my_car.start_engine())