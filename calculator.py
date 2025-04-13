#GITHUB: https://github.com/birkenn/Lab10-CM-NB

import math
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError as error:
        print(str(error))
def hypotenuse(a,b):
    math.hypot(a,b)
def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    try:
        return b/a
    except ZeroDivisionError as error:
        print(str(error))
def logarithm(a,b):
    try:
        return math.log(b,a)
    except ValueError as error:
        print(str(error))
def exp(a,b):
    return a**b
