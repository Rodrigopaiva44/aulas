class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        calc = self.width*self.height
        return calc
    

x = float(input('Width: '))
y = float(input('Height: '))

print(Rectangle(x,y).area())
