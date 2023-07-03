from math import pi

def circle_area(radius):
    if type(radius) not in (int, float):
        raise TypeError("Radius can't be not a number")

    if radius < 0:
        raise ValueError("Radius can't be negative")

    return pi*radius**2
