# basic example of multiple inheritance

class Engine:
    def start_engine(self):
        return "Engine started"
    

class Steering:
    def turn_left(self):
        return "Steering left"
    def turn_right(self):
        return "Steering right"

# the calss inherits from both engine and steering

class Car(Engine, Steering):
    def drive(self):
        return "Car is being driven"
    
# create an instance of car

my_car = Car()

# Access methods from both parent classes
print(my_car.start_engine())
print(my_car.turn_left())
print(my_car.drive())

# print method resolution order(MRO)
print(Car.mro())
print(Car.__mro__)


# method resolution order example

class A:
    def do_something(self):
        return "Doing something in A"
    
class B:
    def do_something(self):
        return "Doing something in B"

class C(A, B):
    def do_something(self):
        return f"{super().do_something()} and C"

# create an instance of C
c = C()
print(C.mro())
print(c.do_something()) # Output: Doing something in A and C

# Explanation
# Class C inherits from both Class A and Class B.
# Class C overrides the do_something method, but it also calls super().do_something() to access the method from Class A. 
# Because of the MRO, super() refers to Class A before Class B.


# Diamond problem

class X:
    def do_something(self):
        return "Doing something in X"

class Y(X):
    def do_something(self):
        return "Doing something in Y"

class Z(X):
    def do_something(self):
        return "Doing something is Z"

class Test(Y, Z):
    pass


# create an instance of Test

test = Test()
print(test.do_something()) # Output: Doing something in B
print(Test.mro()) # Output: [<class '__main__.Test'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.X'>, <class 'object'>]

# Explanation:
# Class D inherits from B and C, both of which inherit from A.
# When d.do_something() is called, Python uses the MRO to resolve the method. In this case, it starts from D, then B, then C, and finally A.
# Therefore, the do_something method from Class B is used.