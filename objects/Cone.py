from math import pi
import random
from Parent import *

class Cone(Parent):
    def input_data(self):
        if self.isTest:
            self.r = random.randint(1, 20)
            self.h = random.randint(1, 20)
            print ("сторона r", self.r)
            print ("высота h", self.h)
        else: 
            self.r = int(input("введите радиус r: "))
            self.h = int(input("введите высоту h: "))
            print("-" * 22)

    def get_square(self):
        if self.isTest:
            q = float("%.2f" % (float(input("введите что насчитали ЧЕРЕЗ ТОЧКУ "))))
            zz = float("%.2f" % ((1/3) * 3.14 * self.r ** 2 * self.h))
            if zz != q:
                return "ответ неверный. объем шара = %f" % zz
            else:
                return "ответ верный. объем шара = %f" % zz

        return round((1/3) * pi * self.r ** 2 * self.h, 2)
        

# cone  = Cone() 
# cone.input_data()
# print(cone.get_square())
# print("-" * 22)