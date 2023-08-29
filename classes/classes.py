# Basic Class Definition
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f"{self.name} says meow!")


# Create an instance of the cat class
cat_1 = Cat("Elt", 5)

# Access attributes and methods
print(f"{cat_1.name} is {cat_1.age} years old.")
cat_1.meow()

# Adding Methods and Encapsulation


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Create an instance of the Rectangle class
rect = Rectangle(5, 3)

# Calculate and display area and perimeter
print("Rectangle Area:", rect.area())
print("Rectangle Perimeter:", rect.perimeter())

#  Inheritance and Polymorphism

# Super class


class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f"This shape is {self.color}.")

# heir class


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# Create instances of Shape and Circle
shape = Shape("blue")
circle = Circle("red", 5)

# Demonstrate inheritance and polymorphism
shape.display_color()
circle.display_color()
print("Circle Area:", circle.area())
