from circle import Circle
from rectangle import Rectangle

figures = [
    Rectangle(1, 2),
    Circle(2),
    Circle(4),
    Rectangle(4, 5)
    ]

for figure in figures:
    area = figure.area()
    print("Area: " + str(area))
    