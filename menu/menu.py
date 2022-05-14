import os
import sys
import json

class Menu:
    mode = None

    def __init__(self):
        with open("./menu/items.json", encoding="utf-8") as file:
            self.items = json.loads(file.read())
    
    def run(self):
        while True:
            os.system("cls")
            while True:
                try:
                    #print("\t\tКАЛЬКУЛЯТОР ПЛОЩАДЕЙ МНОЖЕСТВА ФИГУР")
                    self.mode = int(input("[МЕНЮ]: Выберите режим работы (калькулятор - 1, проверка знаний - 2, выход - 0): "))
                    if not self.mode in [0, 1, 2]:
                        raise Exception
                    break
                except Exception:
                    print("\t[ОШИБКА]: Введенное значение неверное")
                
            if self.mode == 0:
                print("\t[+]: Завершение работы программы...")
                break
                
            self.mode = bool(self.mode - 1)

            print("[МЕНЮ]: Выберите фигуру из списка:")
            for idx, item in enumerate(self.items):
                print("\t%d. %s" % (idx + 1, self.items[item]))
            index = int(input("[МЕНЮ]: Фигура (номер): ")) - 1
            self.current_figure_name = list(self.items.keys())[index]
            self.current_figure_title = list(self.items.values())[index]
            self.current_figure_object = getattr(sys.modules["__main__"],
                self.current_figure_name)(self.current_figure_title, self.mode)
            self.current_figure_object.run()
    
