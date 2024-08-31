Magic Methods in OOP
Magic methods (also known as dunder methods, short for "double underscore") are special methods in Python that start and end with double underscores, like __init__ or __str__. These methods are called implicitly by Python in certain situations, allowing you to define the behavior of your objects in response to built-in operations.

Magic methods allow you to override or extend the behavior of Python's built-in operations and functions, such as arithmetic operations, comparisons, object representation, and more.

Key Concepts of Magic Methods
Special Syntax: Magic methods are named with double underscores (__) at the beginning and end. This distinguishes them from regular methods.
Implicit Invocation: These methods are not called directly by their names. Instead, they are invoked automatically by Python in response to certain operations.
Customization: Magic methods allow you to customize how objects of your class behave with standard Python operations (e.g., adding objects, printing them, or comparing them).


The __new__ method in Python is a special (or "magic") method that is responsible for creating a new instance of a class. It is called before the __init__ method and is used to control the creation of a new instance of a class.

Key Points about __new__:
Instance Creation: The __new__ method is called to create a new instance of a class. It is the method that actually creates and returns a new object.
Called Before __init__: The __new__ method is executed before the __init__ method. While __new__ is responsible for creating the instance, __init__ is responsible for initializing it.
Class Method: Unlike __init__, which takes self as the first argument, __new__ takes cls (the class itself) as the first argument.
Return Value: The __new__ method must return an instance of the class. If it doesn't, then the __init__ method will not be called.
Customization: You rarely need to override __new__. It's typically only overridden in advanced scenarios, such as when implementing singletons, immutable objects, or custom metaclasses.