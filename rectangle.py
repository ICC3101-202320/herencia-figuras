from figure import Figure

class Rectangle(Figure):
    def __init__(self, base, width):
        self._base = base
        self._width = width
    
    def area(self):
        return self._base * self._width
    
    def perimeter(self):
        return 2 * (self._base + self._width)
    