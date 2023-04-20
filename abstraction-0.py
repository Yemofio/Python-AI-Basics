from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
        
rect = Rectangle(10, 20)
circ = Circle(5)

print(rect.area())  # Output: 200
print(circ.area())  # Output: 78.5
