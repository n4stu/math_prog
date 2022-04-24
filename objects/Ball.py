from math import pi
import random
from objects.Parent import Parent

# пофиксить тут вывод правильного ответа с 00000 в тесте
class Ball (Parent):
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
