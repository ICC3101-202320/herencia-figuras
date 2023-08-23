from figure import Figure

class Circle(Figure):
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return self._radius ** 2 * 3.14
    
    def perimeter(self):
        return self._radius * 2 * 3.14
    
    def greet(self):
        return f'Hola soy un círculo con radio {self._radius}'
    