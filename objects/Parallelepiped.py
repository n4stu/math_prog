
import random

class Parallelepiped (Parent):
        
    def input_data(self):
        if self.isTest:
            self.a = random.randint(1, 20)
            self.b = random.randint(1, 20)
            self.c = random.randint(1, 20)
            print ("сторона a", self.a)
            print ("сторона b", self.b)
            print ("сторона c", self.c)        
        else:
            self.a = int(input("введите сторону а: "))
            self.b = int(input("введите сторону b: "))
            self.c = int(input("введите высоту c: "))
            print("-" * 22)

    def get_square(self):
        if self.isTest:
            q = int(input("введите что насчитали"))
            zz = self.a * self.b  * self.c
            return zz == q
        else:
            return self.a * self.b  * self.c
        

# prllpd  = Parallelepiped(bool(int(input("0 калькулятор / 1 тест "))))
# prllpd.input_data()
# print(prllpd.get_square())
# print("-" * 22)