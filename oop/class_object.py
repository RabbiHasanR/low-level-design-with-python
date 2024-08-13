class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
    
    
    def start_engine(self):
        return f"{self.year} {self.make} {self.model}'s engine started."
    
    
    

# creating an object
my_car = Car('Toyota', 'Corolla', 2020)

print(my_car.start_engine())