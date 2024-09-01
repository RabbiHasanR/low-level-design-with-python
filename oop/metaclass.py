# Real-Life Use Case: Enforcing Class Constraints
# Imagine you are designing a framework where certain classes must always include specific methods or properties. 
# You can use a metaclass to enforce these constraints during class creation.

# Example: Enforcing a Class Constraint with a Metaclass
# Suppose you have a requirement that every class in your system must implement a save method. 
# If a class doesn't implement this method, an error should be raised when the class is defined.


# Define a metaclass that enforces a 'save' method
class SaveMethodEnforcer(type):
    def __new__(cls, name, bases, class_dict):
        if 'save' not in class_dict:
            raise TypeError(f"Class {name} must implement a 'save' method")
        return super().__new__(cls, name, bases, class_dict)

# Use the metaclass in a base class
class BaseModel(metaclass=SaveMethodEnforcer):
    def save(self):
        print('basemoel save')

# Example: A valid class
class User(BaseModel):
    def save(self):
        print("User saved")

# Example: An invalid class (will raise an error)
# class Product(BaseModel):
#     pass  # Missing 'save' method, this will raise TypeError

# Uncommenting the following line will raise an error:
# product = Product()  # TypeError: Class Product must implement a 'save' method


# Built-In Example: ABCMeta in the abc Module
# The abc (Abstract Base Class) module in Python uses a metaclass called ABCMeta to define abstract base classes. 
# Abstract base classes are classes that cannot be instantiated directly and are intended to be subclassed. 
# They may define abstract methods that must be implemented by any concrete subclass.

# Example: Using ABCMeta from the abc Module

from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    
    @abstractmethod
    def my_method(self):
        pass


class ConcreateClass(MyAbstractClass):
    def my_method(self):
        print("Implementation of my_method")
        

class IncompleteClass(MyAbstractClass):
    pass


concreate = ConcreateClass()
concreate.my_method()
# Uncommenting the following line will raise an error:
# instance = IncompleteClass()  # TypeError: Can't instantiate abstract class IncompleteClass with abstract method my_method



# Example: Creating a Simple Custom Metaclass

class MyMeta(type):
    def __new__(cls, name, bases, class_dict):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, class_dict)
    
class MyClass(metaclass=MyMeta):
    pass



# In this example, when MyClass is defined, the MyMeta metaclass is called, and it prints a message indicating that the class is being created.


