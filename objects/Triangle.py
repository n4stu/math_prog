from math import radians
import math


class Triangle:
    def __init__(self, isAlfa = False):
        self.isAlfa = isAlfa

    def input_data(self):
        self.a = int(input("Введите сторону a: "))
        if self.isAlfa:
            self.b = int(input("Введите сторону b: "))
            self.alfa = int(input("Введите угол alfa: "))
        else:
            self.h = int(input("Введите высоту: "))
        print("-" * 22)
    
    def get_square(self):
        if self.isAlfa:
            
            return 0.5 * self.a * self.b * math.sin(radians(self.alfa))
        else:
            return 0.5 * self.a * self.h
        
# tr = Triangle(bool(int(input("как считаем тр-к? 0 - по высоте, 1 по сторонам/углу: ")))) # Создаем экземпляр класса Triangle
# tr.input_data()
# print(tr.get_square())
# print("-" * 22)