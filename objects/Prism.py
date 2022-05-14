import random

from objects.Parent import *

class Prism (Parent):
    def run(self):
        self.isH = bool(int(input("\tКак считаем (по высоте - 1, по сторонам - 2): ")) - 1)
        if self.isTest:
            self.h = random.randint(1, 20)
            if self.isH:
                self.a = random.randint(1, 20)
                self.b = random.randint(1, 20)
                print("\tСторона a: ", self.a)
                print("\tСторона b: ", self.b)
            else:
                self.S = random.randint(1, 200)
                print("\tПлощадь основания: ", self.S)
            print("\tВысота h: ", self.h)
        
        else:
            if self.isH:
                self.a = int(input("\tВведите сторону a: "))
                self.b = int(input("\tВведите сторону b: "))
            else:
                self.S = int(input("\tВведите площадь: "))
            self.h = int(input("\tВведите высоту h: "))
        if self.isH:
            self.result = 0.5 * self.a * self.b * self.h
        else:
            self.result = self.S * self.h
        self.calculate()