# Real-World Example: A Car System
# Let's consider a car as an example to demonstrate composition. A car is made up of various components like an engine, tires, and a steering wheel. 
# Each of these components can be represented by a separate class, and the Car class can use composition to include these components.



# compositon design

class Engine:
    def start(self):
        return 'Engine started'
    
    def stop(self):
        return 'Engine stopped'
    

class Tire:
    
    def __init__(self, position) -> None:
        self.position = position
    
    def inflate(self):
        return f"Inflating the {self.position} tire"


class SteeringWheel:
    
    def turn_left(self):
        return 'Turning left'
    def turn_right(self):
        return 'Turning right'
    

class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.tires = [Tire("front-left"), Tire("front-right"), Tire('rear-left'), Tire('rear-right')]
        self.steering_wheel = SteeringWheel()
    
    def drive(self):
        self.engine.start()
        return 'Car is driving'
    
    def stop(self):
        self.engine.stop()
        return 'Car has stopped'
    
    def turn(self, direction):
        if direction == 'left':
            return self.steering_wheel.turn_left()
        elif direction == 'right':
            return self.steering_wheel.turn_right()
    
    def inflate_tires(self):
        return [tire.inflate() for tire in self.tires]
    
    


#use car class

my_car = Car()

print(my_car.drive())
print(my_car.turn('left'))
print(my_car.inflate_tires())
print(my_car.stop())



# Built-In Python Example: The datetime Module
# The datetime module in Python is an example of how composition is used in built-in classes.


from datetime import datetime, date, time

d = date(2023, 7, 10)

t = time(14, 30)

print(d)
print(t)

# use composition to create a datetime object

dt = datetime.combine(d, t)

print(dt)