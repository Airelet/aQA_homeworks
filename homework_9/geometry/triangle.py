from math import sqrt


def perimeter(a: float, b: float, c: float) -> float:
    return round(a + b + c, 2)


def area(a: float, b: float, c: float) -> float:
    s = ((perimeter(a, b, c)) / 2)
    ar = sqrt(s * (s - a) * (s - b) * (s - c))
    return round(ar, 2)

