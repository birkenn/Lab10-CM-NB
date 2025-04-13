import math
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    try:
        return b/a
    except ZeroDivisionError as error:
        print(str(error))
def log(a,b):
    try:
        return math.log(b,a)
    except ValueError as error:
        print(str(error))
def exp(a,b):
    return a**b

import math
def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def logarithm(a,b):
    try:
        return math.log(b,a)
    except ValueError as error:
        print(str(error))
def exponent(a,b):
    return a**b