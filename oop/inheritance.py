# parent class or base class
class Vehicle:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model 
        self.year = year
    
    
    def start_engine(self):
        return f"The engine of the {self.make} {self.model} i starting"
    
    def stop_engine(self):
        return f"The engine of the {self.make} {self.model} is stopping"
    
    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model}"
    


# child calss or derive class
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors) -> None:
        # call the parent class __init__ method
        super().__init__(make=make, model=model, year=year)
        self.num_doors = num_doors
    
    
    def open_trunk(self):
        return f"The trunk of the {self.make} {self.model} is now open"
    
    # ovverriding thes start_engine method
    def start_engine(self):
        return f"The car's engine of the {self.make} {self.model} is starting"
    
    def __str__(self) -> str:
        return f"{super().__str__()} with {self.num_doors} doors"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar) -> None:
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar
    
    def pop_wheelie(self):
        return f"{self.make} {self.model} is popping a wheelie"
    
    def __str__(self) -> str:
        sidecar_status = "With a sidecar" if self.has_sidecar else "without a sidecar"
        return f"{super().__str__()} {sidecar_status}"



# usage example
# creating an instance of car
my_car = Car("Toyota", "Corolla", 2021, 4)
print(my_car)
print(my_car.start_engine())
print(my_car.open_trunk())
print(my_car.stop_engine())



# creating an instance of motorcycle
my_motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2019, False)
print(my_motorcycle)
print(my_motorcycle.start_engine())
print(my_motorcycle.pop_wheelie())
print(my_motorcycle.stop_engine())
