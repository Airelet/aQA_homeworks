from math import pi


def circumference(r: float) -> float:
    return round(2 * pi * r, 2)


def area(r: float) -> float:
    return round(pi * r * r, 2)
