
PI = 3.14159


def circle_area(radius):
    if radius < 0:
        raise Exception('Cannot have a negative-sized circle')
    return PI*radius*radius


def rectangle_properties(length, width):
    if length < 0 or width < 0:
        raise Exception('Cannot have a negative-sized rectangle')
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter