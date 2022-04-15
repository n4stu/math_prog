#n = int(input("МЕНЮ\n\nВыберите:\n\n1.проверка знаний\n2.калькулятор "))
#if n != 1 and n != 2:
 #   print ("Введены неверные значения")
#else:
 #   if n == 1:
  #      print ("1") 
   # else:
    #    print ("2")

menu = {
    "test": {
        "1.": "multi_tables",
        "2.": "square"
    },
    "calculator": {
        "1.": "volume",
        "2.": "area",
        "3.": "equation",
        "4.": "multi_tables",
    }
} 
#for key, value in menu.items():
#    print (key, ":", value)

#print (menu["test"])
#print (menu["calculator"])

print ("введите калькулятор/тест")
n1 = input()

if n1 == 1:
    print ("введите пункт подменю калькулятора")
    #k1 == input ()
else:
    if n1 == 2:
        print ("введите пункт подменю теста")
        k2 == input ()
    else:
        print ("введено неверное значение")