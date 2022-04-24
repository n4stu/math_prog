from math import radians
import math
from random import random
from objects.Parent import Parent

class Parallelogram(Parent):
    def __init__(self, isAlfa = False):
       self.isAlfa = isAlfa

    def input_data(self):
        if self.isTest:
            self.a = random.randint (1, 20)
            print ("сторона a", self.a)
            if self.Alfa:
                self.b = random.randint (1, 20)
                self.alfa = random.randint (1, 20)
                print ("сторона b", self.b)
                print ("угол альфа", self.alfa)
            else:
                self.h = random.randint (1, 20)
                print ("высота h", self.h)
        else:
            self.a = int(input("введите сторону а: "))
            if self.isAlfa:
                self.b  = int(input("введите сторону b: "))
                self.alfa  = int(input("введите угол alfa: "))
            else:
                self.h  = int(input("введите высоту h: "))
            print("-" * 22)

    def get_square(self):
        if self.isTest:
            q = float("%.2f" % (float(input("введите что насчитали ЧЕРЕЗ ТОЧКУ "))))
            zz = 0
            if self.isAlfa:
                zz = float("%.2f" % (self.a * self.b * math.sin(radians(self.alfa))))
            else:
                zz = self.a * self.h
            if zz != q:
                return "ответ неверный. объем шара = %f" % zz
            else:
                return "ответ верный. объем шара = %f" % zz
        else:
            if self.isAlfa:
                return self.a * self.b * math.sin(radians(self.alfa))
            else:
                return self.a * self.h

# prgm = Parallelogram(bool(int(input("как считаем пар-м ? 0 - по высоте, 1 по углу: ")))) 
# prgm.input_data()
# print(prgm.get_square())
# print("-" * 22)