"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    a + b

def sub (a, b):
    a - b

def mul (a, b):
    a*b

def div (a, b):
    b / a  # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError


def log (a,b):
    math.loga(b)
    if a == 0:
        raise ZeroDivisionError

def exp (a, b):
    math.pow(a,b)



