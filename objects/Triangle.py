import math
import random
from math import radians

from objects.Parent import Parent

class Triangle(Parent):

    def run(self):
        self.isAlpha = bool(int(input("\tКак считаем (по высоте - 1, по углу - 2): ")) - 1)
        if self.isTest:
            if self.isAlpha:
                self.a = random.randint(1, 20)
                self.b = random.randint(1, 20)
                self.alfa = random.randint(1, 178)
                print("\tСторона a: ", self.a)
                print("\tСторона b: ", self.b)
                print("\tУгол альфа: ", self.alfa)
            else:
                self.a = random.randint(1, 20)
                self.h = random.randint(1, 20)
                print("\tСторона a: ", self.a)
                print("\tВысота h: ", self.h)
        else:
            self.a = int(input("\tВведите сторону a: "))
            if self.isAlpha:
                self.b = int(input("\tВведите сторону b: "))
                self.alfa = int(input("\tВведите угол alfa: "))
            else:
                self.h = int(input("\tВведите высоту: "))
        if self.isAlpha:
            self.result = 0.5 * self.a * self.b * math.sin(radians(self.alfa))
        else:
            self.result = 0.5 * self.a * self.h
        self.calculate()