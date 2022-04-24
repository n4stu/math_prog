import random
from Parent import *

class Multi_table (Parent):
    from objects.Parent import Parent
    
    def input_data(self):
        if self.isTest:
            self.i = random.randint(1, 10)
            self.j = random.randint(1, 10)
            print ("число i", self.i)
            print ("число j", self.j)
        else:
            self.i = int(input("Введите i: "))
            self.j = int(input("Введите j: "))
        print ("-" * 22)
        
    
    def get_square(self):
        if self.isTest:
            q = int(input("введи что насчитали "))
            zz = self.i * self.j 
            return zz == q
            
        else:
            return self.i * self.j 


# multi = Multi_table(bool(int(input("0 калькулятор / 1 тест ")))) 
# multi.input_data()
# print(multi.get_square())
# print("-" * 22) 