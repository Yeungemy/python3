class Cylinder:
    pi = 3.14

    def __init__(self, height = 1, radius = 1) -> None:
        self.height = height
        self.radius = radius

    def volume(self):
        v = self.pi * self.radius**2 * self.height
        print("the volume of the cylinder is {}".format(v))

        return v

    def surface_area(self):
        sa = 2 * self.pi * self.radius**2 + 2 * self.pi * self.radius * self.height
        print("the surface area of the cylinder is {}".format(sa))

        return sa