from math import pi

from Parent import *

class Cone(Parent):
    def input_data(self):
        print ("посчитаем объем конкуса  ")    
        self.r = int(input("введите радиус r: "))
        self.h = int(input("введите высоту h: "))
        print("-" * 22)

    def get_square(self):
        return round((1/3) * pi * self.r ** 2 * self.h, 2)
        

# cone  = Cone() 
# cone.input_data()
# print(cone.get_square())
# print("-" * 22)