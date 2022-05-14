import random

from objects.Parent import Parent

class Cylinder(Parent):
    def run(self):
        if self.isTest:
            self.r = random.randint(1, 20)
            self.h = random.randint(1, 20)
            print("\tРадиус r: ", self.r)
            print("\tВысота h: ", self.h)
        else:
            self.r = int(input("\tВведите радиус: "))
            self.h = int(input("\tВведите высоту: "))
        self.result = 3.14 * self.r ** 2 * self.h
        self.calculate()