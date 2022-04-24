#   ПРОВЕРИТЬ ТЕСТ НА ПРЯМОУГОЛЬНИК/КВАДРАТ

import random
from objects.Parent import Parent

class Rectangle(Parent):
    def __init__(self, isRectangle = False):
        self.isRectangle = isRectangle

    def input_data(self):
        if self.isTest:
            self.a = random.randint(1, 20)
            print ("сторона a", self.a)
            if self.isRectangle:
                self.b = random.randint(1, 20)
                print ("сторона b", self.b)
        else:
            self.a = int(input("Введите сторону a: "))
            if self.isRectangle:
                self.b = int(input("Введите сторону b: "))
            else:
                self.b = self.a
            print("-" * 22)

    def get_square(self):
        if self.isTest:
            q = int(input("введите что насчитали"))
            zz = self.a * self.b
            return zz == q
        return self.a * self.b
   

# rct = Rectangle(bool(int(input("что считаем? 0 - квадрат, 1 прямоугольник: ")))) 
# rct.input_data()
# print(rct.get_square())
# print("-" * 22)