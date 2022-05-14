from objects.Parent import Parent
import random

class Trapezoid(Parent):
    def run(self):
        if self.isTest:
            self.a = random.randint(1, 20)
            self.b = random.randint(1, 20) 
            self.h = random.randint(1, 20)
            print("\tСторона a:", self.a)
            print("\tСторона b:", self.b)
            print("\tСторона h:", self.h)
        else:
            self.a = int(input("\tВведите сторону а: "))
            self.b = int(input("\tВведите сторону b: "))
            self.h = int(input("\tВведите высоту h: "))
        self.result = 0.5 * (self.a + self.b ) * self.h
        self.calculate()