#   ПРОВЕРИТЬ ТЕСТ НА ПРЯМОУГОЛЬНИК/КВАДРАТ

import random

from objects.Parent import Parent

class Rectangle(Parent):
    def run(self):
        if self.isTest:
            self.a = random.randint(1, 20)
            self.b = random.randint(1, 20)
            print("\tСторона a: ", self.a)
            print("\tСторона b: ", self.b)
        else:
            self.a = int(input("\tВведите сторону a: "))
            self.b = int(input("\tВведите сторону b: "))
        self.result = self.a * self.b
        self.calculate()