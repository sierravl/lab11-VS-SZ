# https://github.com/sierravl/lab11-VS-SZ.git
# Partner 1: Vanessa Sierra
# Partner 2: Sophie Zalamar

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example
import math

def add(a, b):
    return a + b

def sub (a, b):
    return a - b

def subtract(a,b):
    return sub(a,b)

def mul (a, b):
    return a*b

def div (a, b):
      # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError
    return b/a

def log (a,b):
    if a <= 0 or a ==1 or b<=0:
        raise ValueError
    return math.log(b,a)

def logarithm (a,b):
    return log(a,b)

def exp (a, b):
    return a**b

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError

def hypotenuse(a,b):
    return round(math.hypot(a,b))  #can have negative nums