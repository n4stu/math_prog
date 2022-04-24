from math import radians
import math
import random
from objects.Parent import Parent

class Triangle(Parent):
    def __init__(self, isAlfa = False):
        self.isAlfa = isAlfa
 
    def input_data(self):
        if self.isTest:
            if self.isAlfa:
                self.a = random.randint (1, 20)
                self.b = random.randint (1, 20)
                self.alfa = random.randint (1, 20)
                print ("сторона a", self.a)
                print ("сторона b", self.b)
                print ("угол альфа", self.alfa)
            else:
                self.a = random.randint (1, 20)
                self.h = random.randint (1, 20)
                print ("сторона a", self.a)
                print ("высота h", self.h)
        else:
            self.a = int(input("Введите сторону a: "))
            if self.isAlfa:
                self.b = int(input("Введите сторону b: "))
                self.alfa = int(input("Введите угол alfa: "))
            else:
                self.h = int(input("Введите высоту: "))
            print("-" * 22)
        
    def get_square(self):
        if self.isTest:
            q = float("%.2f" % (float(input("введите что насчитали ЧЕРЕЗ ТОЧКУ "))))
            zz = 0
            if self.isAlfa:
                zz = float("%.2f" % (0.5 * self.a * self.b * math.sin(radians(self.alfa))))
            else:
                zz = 0.5 * self.a * self.h
            if zz != q:
                return "ответ неверный. объем шара = %f" % zz
            else:
                return "ответ верный. объем шара = %f" % zz
        if self.isAlfa:
            
            return 0.5 * self.a * self.b * math.sin(radians(self.alfa))
        else:
            return 0.5 * self.a * self.h
        
# tr = Triangle(bool(int(input("как считаем тр-к? 0 - по высоте, 1 по сторонам/углу: ")))) # Создаем экземпляр класса Triangle
# tr.input_data()
# print(tr.get_square())
# print("-" * 22)