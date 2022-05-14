import random

from objects.Parent import *

class Multiplicator(Parent):
    def run(self):
        if self.isTest:
            self.a = random.randint(1, 10)
            self.b = random.randint(1, 10)
            print("\tЧисло a: ", self.a)
            print("\tЧисло b: ", self.b)
        else:
            self.a = int(input("\tВведите a: "))
            self.b = int(input("\tВведите b: "))
        self.result = float(self.a * self.b)
        self.calculate()