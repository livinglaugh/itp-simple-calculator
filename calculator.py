def add(x, y):
    if type(x) != int or type(y) != int:
        return None
    else:
        return x + y


def subtract(x, y):
    if type(x) != int or type(y) != int:
        return None
    else:
        return x - y


def divide(x, y):
    if type(x) != int or type(y) != int:
        return None
    elif x = 0 or y = 0:
        return "Invalid value for denominator, can't divide by 0!"
    else:
        return x / y
    


def multiply(x, y):
    if type(x) != int or type(y) != int:
        return None
    else:
        return x * y
    


def square(x):
    if type(x) != int:
        return None
    else:
        return x ** 2
    


def power(x, y):
    if type(x) != int or type(y) != int:
        return None
    else:
        return x ** y
    


def sqrt(x):
    if type(x) != int:
        return None
    else:
        return math.sqrt(x)
    
