from math import radians, pi
import math
import random

from objects.Cylinder import *

class Parent:
    def __init__(self, isTest = False):
        self.isTest = isTest

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


class Rectangle:
    def __init__(self, isAlfa = False):
        self.isAlfa = isAlfa

    def input_data(self):
        self.a = int(input("Введите сторону a: "))
        if self.isAlfa:
            self.b = int(input("Введите сторону b: "))
        else:
            self.b = self.a
        print("-" * 22)
    
    def get_square(self):
        return self.a * self.b
   

# rct = Rectangle(bool(int(input("что считаем? 0 - квадрат, 1 прямоугольник: ")))) 
# rct.input_data()
# print(rct.get_square())
# print("-" * 22)


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




class Trapezoid:
    def input_data(self):
        print ("посчитаем трапезоид  ")    
        self.a = int(input("введите сторону а: "))
        self.b = int(input("введите сторону b: "))
        self.h = int(input("введите высоту h: "))
        print("-" * 22)

    def get_square(self):
        return 0.5 * (self.a + self.b ) * self.h
        
# trap  = Trapezoid() 
# trap.input_data()
# print(trap.get_square())
# print("-" * 22)



class Parallelepiped:
    def input_data(self):
        print ("посчитаем объем параллелепипед  ")    
        self.a = int(input("введите сторону а: "))
        self.b = int(input("введите сторону b: "))
        self.c = int(input("введите высоту c: "))
        print("-" * 22)

    def get_square(self):
        return self.a * self.b  * self.c


        

# prllpd  = Parallelepiped() 
# prllpd.input_data()
# print(prllpd.get_square())
# print("-" * 22)



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




# пофиксить тут вывод правильного ответа с 00000 в тесте
class Ball:
    def __init__(self, isTest = False):
        self.isTest = isTest
    def input_data(self):
        if self.isTest:
            self.r = random.randint(1, 20)
            print ("сторона r", self.r)
        else: 
            self.r = int(input("введите радиус r: "))
            print("-" * 22)

    def get_square(self):
        if self.isTest:
            q = float("%.2f" % (float(input("введите что насчитали ЧЕРЕЗ ТОЧКУ "))))
            zz = float("%.2f" % ((4/3) * 3.14 * self.r ** 3))
            if zz != q:
                return "ответ неверный. объем шара = %f" % zz
            else:
                return "ответ верный. объем шара = %f" % zz

        else:
            return round((4/3) * pi * self.r ** 3, 2)
        

# ball  = Ball(bool(int(input("0 калькулятор / 1 тест ")))) 
# ball.input_data()
# print(ball.get_square())
# print("-" * 22)



# пофиксить тут вывод правильного ответа с 00000 в тесте
class Сylinder (Parent):
    def input_data(self):
        if self.isTest:
            self.r = random.randint(1, 20)
            self.h = random.randint(1, 20)
            print ("сторона r", self.r)
            print ("сторона h", self.h)
        else:   
            self.r = int(input("введите радиус r: "))
            self.h = int(input("введите высоту h: "))
            print("-" * 22)

    def get_square(self):
        if self.isTest:
            q = float("%.2f" % (float(input("введите что насчитали ЧЕРЕЗ ТОЧКУ "))))
            zz = float("%.2f" % (pi * self.r ** 2 * self.h))
            if zz != q:
                return "ответ неверный. объем шара = %f" % zz
            else:
                return "ответ верный. объем шара = %f" % zz
        

# cyl  = Сylinder(bool(int(input("0 калькулятор / 1 тест ")))) 
# cyl.input_data()
# print(cyl.get_square())
# print("-" * 22)





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



class Multi_table (Parent):
    # def __init__(self, isTest = False ):
    #     self.isTest = isTest
        

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