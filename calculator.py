#GITHUB LINK: https://github.com/birkenn/Lab10-CM-NB
import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Cannot calculate square root of a negative number")

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return b / a  
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")

def logarithm(b, a=10):  # 'a' is the base, default is 10
    try:
        return math.log(b, a)
    except ValueError:
        raise ValueError("Invalid input for logarithm")

def exp(a, b):
    return a ** b