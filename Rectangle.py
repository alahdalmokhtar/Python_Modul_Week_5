class Rectangle:
    def __init__ (self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    
Rectangle1 = Rectangle(10, 20)
print ("Area of Rectangle1:", Rectangle1.area())
print ("Perimeter of Rectangle1:", Rectangle1.perimeter())
