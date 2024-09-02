# Example 1: Avoiding Code Duplication
# Consider you have a system where you need to calculate taxes for different types of products. A non-DRY approach might look like this:


def calculate_tax_food(price):
    tax_rate = 0.07
    return price * (1+tax_rate)


def calculate_tax_clothing(price):
    tax_rate = 0.12
    return price * (1+tax_rate)

def calculate_tax_electronics(price):
    tax_rate = 0.15
    return price * (1+tax_rate)


# This code is repetitive and cumbersome. Let's DRY it up:

def calculate_tax(price, tax_rate):
    return price * (1 + tax_rate)


#usage
food_tax = calculate_tax(100, 0.07)
clothing_tax = calculate_tax(100, 0.12)
electronics_tax = calculate_tax(100, 0.15)

# Here, a single function handles all product types, and the tax rate is passed as a parameter, embodying the DRY principle.

# Example 2: Using Decorators for Cross-cutting Concerns
# Suppose you need to log function calls in multiple functions. Instead of writing the logging code in each function, use a decorator


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)
    
    return wrapper


@logger
def add(a,b):
    return a+b

@logger
def multiply(a,b):
    return a * b


# usage 
add_result = add(3,4)
multiply_result = multiply(3,4)


# In this example, the logger decorator is applied to any function that needs logging, significantly reducing repetitive logging code.