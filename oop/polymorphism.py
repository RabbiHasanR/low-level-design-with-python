# method overriding (Runtime Polymorphism)

class Animal:
    def speak(self):
        return 'Some generic animal sound'


class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


class Bird(Animal):
    def speak(self):
        return "Chirp"


# usage

animals = [Dog(), Cat(), Bird()]

for animal in animals:
    print(animal.speak())
    


# Explanation:
# Method Overriding: Each subclass (Dog, Cat, Bird) overrides the speak() method from the Animal class. When speak() is called on an instance of Dog, Cat, or Bird, the appropriate version of speak() is executed.
# Polymorphism in Action: The loop iterates over a list of different animal objects, and despite calling the same method speak(), different outputs are produced based on the object's type.


# Operator Overloading

# Scenario: Consider you’re working with vectors (2D points) in a graphics application. You want to add two vectors together using the + operator, which normally works with numbers.

class Vector:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)
    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    

# usage
v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2 # Uses the __add__ method

print(v3) # Output: Vector(6, 8)

# Explanation:
# Operator Overloading: The + operator is overloaded in the Vector class to add the x and y components of two vectors. The __add__ method is a special method that Python uses for the + operator.
# Polymorphism in Action: The + operator works differently depending on the type of objects it is applied to. In this case, it adds two Vector objects.


# Method Overloading

# Scenario: Let’s say you’re building a utility class that handles different types of data (e.g., strings, lists) and needs a method process() that works differently based on the input type.

class DataProcessor:
    def process(self, data=None):
        if isinstance(data, str):
            return data.upper()
        elif isinstance(data, list):
            return [item * 2 for item in data]
        else:
            return "Unsupported data type"
        


# usage
processor = DataProcessor()

print(processor.process("hello"))
print(processor.process([1,2,3]))
print(processor.process(42))


# Explanation:
# Method Overloading (Simulated): Python does not support method overloading in the traditional sense (like in Java or C++), but you can achieve a similar effect using default arguments and type checking inside a method.
# Polymorphism in Action: The process() method behaves differently based on the type of the input data.

# Polymorphism with abastract base classes (ABC)


from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount} using credit card"


class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal"


# usage
payments = [CreditCardPayment(), PayPalPayment()]

print(CreditCardPayment, PayPalPayment,)
for payment in payments:
    print(payment.pay(100))
    

# Explanation:
# Abstract Base Class (ABC): PaymentMethod is an abstract base class that defines a common interface (pay()) for all payment methods. Subclasses like CreditCardPayment and PayPalPayment must implement the pay() method.
# Polymorphism in Action: The pay() method is called on different objects (CreditCardPayment and PayPalPayment), and the appropriate method is executed based on the object type.
