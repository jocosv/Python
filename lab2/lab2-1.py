class Rectangle:
    length = 1
    width = 1

    def set(self, x, y):
        if 0.0 < x < 20.0:
            self.length = x
        else:
            print("error, out of bounds...")
            exit(1)
        if 0.0 < y < 20.0:
            self.width = y
        else:
            print("error, out of bounds...")
            exit(1)

    def get(self):
        return str(self.length) + ' ' + str(self.width)

    def perimeter(self):
        return self.length*2 + self.width*2

    def area(self):
        return self.length*self.width


obj = Rectangle()
print(obj.get())
obj.set(11, 17)
print(obj.get())
print("perimeter of rectangle: ", obj.perimeter())
print("area of rectangle: ", obj.area())


