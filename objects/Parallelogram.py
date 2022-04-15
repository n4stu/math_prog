from math import radians
import math

class Parallelogram:
    def __init__(self, isAlfa = False):
       self.isAlfa = isAlfa

    def input_data(self):
        self.a = int(input("введите сторону а: "))
        if self.isAlfa:
            self.b  = int(input("введите сторону b: "))
            self.alfa  = int(input("введите угол alfa: "))
        else:
            self.h  = int(input("введите высоту h: "))
        print("-" * 22)

    def get_square(self):
        if self.isAlfa:
            
            return self.a * self.b * math.sin(radians(self.alfa))
        else:
            return self.a * self.h

# prgm = Parallelogram(bool(int(input("как считаем пар-м ? 0 - по высоте, 1 по углу: ")))) 
# prgm.input_data()
# print(prgm.get_square())
# print("-" * 22)