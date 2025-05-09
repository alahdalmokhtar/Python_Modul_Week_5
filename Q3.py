class Shape: 
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def area_calculate(self):
        return self.width * self.height

class Squere(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def area_calculate(self):
        return self.width * self.height
    

recangular = Rectangle(10, 20)
squere = Squere(10, 10)
print("Area of Rectangle:", recangular.area_calculate())
print("Area of Squere:", squere.area_calculate())