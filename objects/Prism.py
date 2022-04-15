from Parent import *

class Prism (Parent):
    
    def __init__(self, isTest = False, isH = False):
        super().__init__(isTest)
        self.isH = isH

    def input_data(self):
        if self.isTest:
            if self.isH:
                self.a = random.randint(1, 20)
                self.b = random.randint(1, 20)
                self.h = random.randint(1, 20)
                print ("сторона a", self.a)
                print ("сторона b", self.b)
                print ("сторона h", self.h)
            else:
                self.S = random.randint(1, 200)
        
        else:
            if self.isH:
                self.a = int(input("Введите сторону a: "))
                self.b = int(input("Введите сторону b: "))
                self.h = int(input("Введите высоту h: "))
            else:
                self.S = int(input("Введите площадь: "))
        print ("-" * 22)
        
    
    def get_square(self):
        if self.isTest:
            q = int(input("введи что насчитали"))
            if self.isH:
                zz = 0.5 * self.a * self.b * self.h
                return zz == q
            else:
                zz = self.S* self.h 
                return zz == q
        else:
            if self.isH:
                return 0.5 * self.a * self.b * self.h 
            else:
                return self.S* self.h 


# prism = Prism(bool(int(input("0 калькулятор / 1 тест "))), bool(int(input("0 площадь / 1 стороны ")))) 
# prism.input_data()
# print(prism.get_square())
# print("-" * 22) 