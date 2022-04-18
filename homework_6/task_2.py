from math import sqrt


def square(argument: int):
    result = (argument * 4, argument ** 2, sqrt(2) * argument)
    return result


print(square(3))
