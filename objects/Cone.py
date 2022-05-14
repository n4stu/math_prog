import random

from objects.Parent import *

class Cone(Parent):
    def run(self):
        if self.isTest:
            self.r = random.randint(1, 20)
            self.h = random.randint(1, 20)
            print("\tСторона r: ", self.r)
            print("\tВысота h: ", self.h)
        else: 
            self.r = int(input("\tВведите радиус r: "))
            self.h = int(input("\tВведите высоту h: "))
        self.result = (1/3) * 3.14 * self.r ** 2 * self.h
        self.calculate()