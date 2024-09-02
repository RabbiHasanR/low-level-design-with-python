# Example: Calculating Factorial
# Overly Complex:

def factorial(n):
    result = 1
    if n < 0:
        return "Factorial undefiend for negative numbers"
    elif n == 0:
        return 1
    
    else:
        for i in range(2, n + 1):
            result *= i
    return i


# KISS aligned

import math

def factorial(n):
    if n < 0:
        return "Factorial undefiend for negative numbers"
    else:
        return math.factorial(n)
    
    
# The KISS-adherent version leverages the built-in math.factorial function, making the code more concise, readable, and likely more efficient.