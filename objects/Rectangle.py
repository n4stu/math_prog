

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