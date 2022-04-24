import random
from objects.Parent import Parent
from math import pi

class Cylinder(Parent):
    def input_data(self):
        if self.isTest:
            self.r = random.randint(1, 20)
            self.h = random.randint(1, 20)
            print ("радус r", self.r)
            print ("высота h", self.h)
        else:
            self.r = int(input("введите радиус"))
            self.h = int(input("введите высоту"))
            print("-" * 22)

    def get_square(self):
        if self.isTest:
            q = float("%.2f" % (float(input("введите что насчитали ЧЕРЕЗ ТОЧКУ "))))
            zz = float("%.2f" % ( 3.14 * self.r ** 2 * self.h))
            if zz != q:
                return "ответ неверный. объем шара = %f" % zz
            else:
                return "ответ верный. объем шара = %f" % zz
        return  round( pi * self.r ** 2 * self.h, 2)

cylinder = Cylinder()
cylinder.input_data()
print(cylinder.get_square)
print("-" * 22)
