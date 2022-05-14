import random

from objects.Parent import Parent

class Ball (Parent):
    def run(self):
        if self.isTest:
            self.r = random.randint(1, 20)
            print("\tРадиус r: ", self.r)
        else: 
            self.r = int(input("\tВведите радиус r: "))
        self.result = (4/3) * 3.14 * self.r ** 3
        self.calculate()