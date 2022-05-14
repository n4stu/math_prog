import random

from objects.Parent import Parent

class Parallelepiped (Parent):
    def run(self):
        if self.isTest:
            self.a = random.randint(1, 20)
            self.b = random.randint(1, 20)
            self.c = random.randint(1, 20)
            print("\tСторона a: ", self.a)
            print("\tСторона b: ", self.b)
            print("\tСторона c: ", self.c)        
        else:
            self.a = int(input("\tВведите сторону а: "))
            self.b = int(input("\tВведите сторону b: "))
            self.c = int(input("\tВведите высоту c: "))
        self.result = self.a * self.b  * self.c
        self.calculate()