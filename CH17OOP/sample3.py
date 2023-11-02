class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        area = self.length * self.width
        return area
    
    def perimeter(self):
        perimeter = (2 * self.length) +  (2 * self.width) 
        return perimeter
    
    
rectangle1 = Rectangle(length=12, width=6)
print(f"The area of the rectangle with width {rectangle1.width} and length {rectangle1.length} is {rectangle1.area()}")
print(f"The perimeter of the rectangle with width {rectangle1.width} and length {rectangle1.length} is {rectangle1.perimeter()}")
