class Parent:
    def __init__(self, title, isTest = False):
        self.title = title
        self.isTest = isTest
        self.isFinish = False
        print("Выбранная фигура %s" % self.title)
    
    def get_user_result(self, result):
        while True:
            try:
                self.user_result = input("Введите результат (если число целое - указать до десятых (Например, 5.0)): ")
                if not isinstance(float(self.user_result), float):
                    raise Exception
                break
            except Exception:
                print("\t[ОШИБКА]: Введенное значение не соответсвует формату")
        
        if self.user_result == str(result):
            print(f"\t[%s]: Ответ верный" % self.title)
        else:
            print(f"\t[%s]: Ответ неверный. Результат: %.1f" % (self.title, result))
    
    def calculate(self):
        if self.isTest:
            self.get_user_result(self.result)
        else:
            print(f"Результат: %.1f" % self.result)
        input("\tНажмите любую клавишу...")