"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math

def square_root(a):
    try:
        math.sqrt(a)
    except a < 0:
        raise ValueError

def hypotenuse(a,b):
    try:
        math.hypot(a,b)  #can have negative nums

def add(a, b): 
    a + b

def sub(a, b):
    a - b

def mul(a, b):
    a * b

def div(a, b):
    b / a
    if a == 0:
        raise ZeroDivisionError

def log(a, b):
    math.log(b, a)
    if b <= 0:
        raise ValueError

def exp(a,b):
    math.pow(a, b)