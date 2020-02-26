class Circle:

    def calculate_area(self):
        print("Enter the radius of circle: ")
        self.s = float(input())
        area = 3.14*self.s*self.s
        print("Area of circle is %f" % (area))

    def calculate_perimeter(self):
        perimeter = 2*3.14*self.s
        print("Perimeter of circle is %f" % (perimeter))


class Rectangle:

    def calculate_area(self):
        print("Enter the length of rectangle: ")
        self.a = float(input())
        print("Enter the breadth of rectangle: ")
        self.b = float(input())
        area = self.a*self.b
        print("Area of rectangle is %f" % (area))

    def calculate_perimeter(self):
        perimeter = 2*(self.a+self.b)
        print("Perimeter of rectangle is %f" % (perimeter))

class Square:

    def calculate_area(self):
        print("Enter the side of square: ")
        self.s = float(input())
        area = self.s*self.s
        print("Area of square is %f" % (area))

    def calculate_perimeter(self):
        perimeter = 4*self.s
        print("Perimeter of square is %f" % (perimeter))

c = Circle()
c.calculate_area()
c.calculate_perimeter()

r = Rectangle()
r.calculate_area()
r.calculate_perimeter()

s = Square()
s.calculate_area()
s.calculate_perimeter()
