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