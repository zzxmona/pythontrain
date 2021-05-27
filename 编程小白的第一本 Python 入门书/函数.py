import numpy

def fahrenheit_converter(C):
    fahrenheit = C * 9 / 5 + 32
    return str(fahrenheit) + '˚F'


print(fahrenheit_converter(5))
print(numpy.cos(30))
