import math

class Shape:
    all = []        
    def __init__(self, color):
        self.__color = color
        Shape.all.append(self)
    def __repr__(self):
        return f"{self.__class__.__name__} has a perimeter of {self.calculate_perimeter()} and area of {self.calculate_area()}."
    def calculate_perimeter(self):
        pass
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.__radius = radius
    def get_radius(self):
        return self.__radius
    def set_radius(self, radius):
        self.__radius = radius
    def calculate_area(self):
        return math.pi * self.__radius**2
    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius
    
class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.__length = length
        self.__width = width
    def get_length(self):
        return self.__length
    def set_length(self, length):
        self.__length = length
    def get_width(self):
        return self.__width
    def set_width(self, width):
        self.__width = width
    def calculate_area(self):
        return self.__length * self.__width
    def calculate_perimeter(self):
        return 2 * self.__length + 2 * self.__width
class Triangle(Shape):
    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
    def get_length(self):
        return [self.__side1, self.__side2, self.__side3]
    def set_length(self, side1, side2, side3):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
    def calculate_area(self):
        s = .5 * self.calculate_perimeter()
        return math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))
    def calculate_perimeter(self):
        return self.__side1 + self.__side2 + self.__side3
    
shape1 = Circle("red", 5)
shape2 = Rectangle("blue", 8, 5)
shape3 = Triangle("white", 4,5,6)
shape4 = Circle("purple", 8)
shape5 = Rectangle("cyan", 2, 3)
shape6 = Triangle("orange", 1, 3, 4)

for shape in Shape.all:
    print(shape)


    