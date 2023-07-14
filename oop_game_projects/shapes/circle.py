class Circle():
    # class object atribute
    pi = 3.14

    def __init__(self, circumference, area, radius = 1) -> None:
        self.radius = radius
        self.circumference = 2 * radius * self.pi
        self.area = self.pi * radius**2
    
