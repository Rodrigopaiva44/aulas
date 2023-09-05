class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

# Exemplo de uso das classes


circle = Circle(5)
triangle = Triangle(6, 8)

print("Área do círculo:", circle.calculate_area())
print("Área do triângulo:", triangle.calculate_area())
