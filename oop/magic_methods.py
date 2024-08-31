# Common Magic Methods and Their Use Cases
# Here’s a detailed look at some of the most commonly used magic methods, along with examples and real-life use cases.

# 1. __init__: Object Initialization
# Purpose: The __init__ method is called when an instance of a class is created. It allows you to initialize the object with specific attributes.

from typing import Any


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


# creating an object
person = Person('John', 30)
print(person.name, person.age) # output: John 30

# Real-Life Use Case: When creating an object representing a user in a system, the __init__ method initializes the user with attributes like name, age, email, etc.


# 2. __str__ and __repr__: Object Representation
# Purpose:

# __str__: Defines how an object is represented as a string, typically for display to the end-user.
# __repr__: Defines how an object is represented in an unambiguous way, typically for debugging.
# Example:

class PersonTwo:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age='{self.age}')"
    
    

persontwo = PersonTwo('John', 30)

print(person)  # Output: John, 30 years old
print(repr(person))  # Output: Person(name='John', age=30)

# Real-Life Use Case: Customizing how objects are displayed in user interfaces, logging systems, or debugging tools.


# 3. __add__, __sub__, __mul__, etc.: Operator Overloading
# Purpose: Magic methods like __add__, __sub__, __mul__, etc., allow you to define how objects of your class interact with arithmetic operators.

# Example:


class Vector:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    
    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)
    
    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    
    

v1 = Vector(2,3)
v2 = Vector(4,5)
v3 = v1 + v2
v4 = v2 - v1
v5 = v3 * v4

print(v3) # output: Vector(6,8)

print(v4) #output: Vector(2,2)

print(v5) #output: Vector(12, 16)

# Real-Life Use Case: Implementing mathematical operations on custom data types like vectors, matrices, complex numbers, etc.


# 4. __eq__, __lt__, __gt__, etc.: Comparison Operations
# Purpose: Magic methods like __eq__ (equality), __lt__ (less than), __gt__ (greater than), etc., allow you to define how objects of your class are compared.

# Example:

class PersonThree:
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def __eq__(self, value: object) -> bool:
        return self.name == value.name and self.age == value.age
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __gt__(self, other):
        return self.age > other.age
    

personthree1 = PersonThree('Alice', 25)
personthree2 = PersonThree('Bob', 30)

print(personthree1 == personthree2) # Output: False
print(personthree1 < personthree2) # Output: True
print(personthree1 > personthree2) # Output: False

# Real-Life Use Case: Sorting objects, comparing records in databases, or implementing business rules that depend on object comparisons.


# 5. __getitem__, __setitem__, __delitem__: Container Operations
# Purpose: Magic methods like __getitem__, __setitem__, and __delitem__ allow you to define how objects of your class interact with indexing and item assignment.

# Example:

class CustomerList:
    
    def __init__(self) -> None:
        self.items = []
        
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
        
    def __delitem__(self, index):
        del self.items[index]
        


clist = CustomerList()
clist.items = [1,2,3,4]

print(clist[1]) #output: 2
# print(clist[8]) #error: list indec out of range

clist[1] = 20
print(clist[1]) # output: 20
# clist[9] = 10  # error: list assignment index out of range

del clist[1]
print(clist.items) # output: [1,3,4]


# Real-Life Use Case: Implementing custom data structures that behave like Python’s built-in lists, dictionaries, or other containers.



# 6. __call__: Callable Objects
# Purpose: The __call__ method allows an instance of a class to be called as if it were a function.

# Example:


class Multiplier:
    
    def __init__(self, factor) -> None:
        self.factor = factor

    def __call__(self, x) -> Any:
        return self.factor * x


double = Multiplier(5)

print(double(6)) # output: 30

# Real-Life Use Case: Implementing objects that can be used as functions, such as creating custom decorators or callbacks.


# 7. __len__, __iter__, __next__: Iterable and Iterator Protocols
# Purpose:

# __len__: Defines how the length of an object is calculated.
# __iter__: Returns an iterator object for the class.
# __next__: Defines the behavior of the iterator when iterating over the object.
# Example:

class MyRange:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        
        
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1
    
    def __len__(self):
        return max(0, self.end - self.start)
    

my_range = MyRange(1,5)

print(len(my_range)) # output: 4

for num in my_range:
    print(num)  # output: 1 2 3 4
    
    

# Real-Life Use Case: Implementing custom iterable objects, such as custom ranges, data streams, or sequences.


# 8. __enter__ and __exit__: Context Managers
# Purpose: These methods allow an object to be used with the with statement, managing the setup and cleanup code.

# Example:
    
class FileManager:
    def __init__(self, filename, mode) -> None:
        self.filename = filename
        self.mode = mode
    
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        

with FileManager("test.txt", "w") as f:
    f.write("Hello, world")
    

# Real-Life Use Case: Managing resources like file handling, database connections, or network connections, ensuring they are properly initialized and closed.


# Basic Example of __new__:
# Here’s a simple example to demonstrate how __new__ works:


class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating instance of MyClass")
        instance = super(MyClass, cls).__new__(cls)  # Call the base __new__ method to create an instance
        return instance

    def __init__(self, value):
        print("Initializing instance of MyClass")
        self.value = value

# Example usage
obj = MyClass(10)

# output:
# Creating instance of MyClass
# Initializing instance of MyClass


# Use Cases for __new__:
# While __new__ is rarely overridden in typical object-oriented programming, there are some scenarios where it is useful:

# Creating Immutable Objects: In classes where instances should be immutable (like int, str, tuple), __new__ is used to control the instance creation without allowing changes after creation.

# Implementing Singletons: A singleton is a design pattern where a class only allows a single instance to be created. This can be enforced using __new__.

# Custom Metaclasses: Advanced use cases involving metaclasses might require overriding __new__ to control how instances of a class are created.


# Example: Singleton Pattern
# Here’s an example of how you might use __new__ to implement the Singleton pattern:


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value
    


# example usage
singleton1 = Singleton(10)

singleton2 = Singleton(20)

print(singleton1.value)  # Output: 20
print(singleton2.value)  # Output: 20
print(singleton1 is singleton2)  # Output: True

