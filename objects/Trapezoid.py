from objects.Parent import Parent
from random import random
class Trapezoid(Parent):
    def input_data(self):
        if self.isTest:
            self.a = random.randint (1, 20)
            self.b = random.randint (1, 20) 
            self.h = random.randint (1, 20)
            print ("сторона a", self.a)
            print ("сторона b", self.b)
            print ("сторона h", self.h)
        else:
            self.a = int(input("введите сторону а: "))
            self.b = int(input("введите сторону b: "))
            self.h = int(input("введите высоту h: "))
            print("-" * 22)

    def get_square(self):
        if self.isTest:
            q = input("введите, что насчитали")
            zz = 0.5 * (self.a + self.b ) * self.h
            if zz != q:
                return "ответ неверный. объем шара = %f" % zz
            else:
                return "ответ верный. объем шара = %f" % zz
        else:
            return 0.5 * (self.a + self.b ) * self.h
        
# trap  = Trapezoid() 
# trap.input_data()
# print(trap.get_square())
# print("-" * 22)