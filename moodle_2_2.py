first=input('Введите 1 число: ') # Организуем ввод 1 числа
second=input('Введите 2 число: ')# Организуем ввод 2 числа
third=input('Введите 3 число: ')# Организуем ввод 3 числа
print (first )# Выводим на экран 1 число
print (second )#Выводим на экран 2 число
print (third )#Выводим на экран 3 число
if first == second and second== third:# Сравниваем 1-2 и 2-3 между собой с
                                      # обязательным соблюдением равенства
    print(" Все числа равны индекс: 3")# выводим на экран индекс 3
elif first==second or  second == third or first == third:#Сравниваем 1-2, 2-3 и 1-3
                       # числа между собой с хотябы одним соблюдением равенства
    print('Равны два числа индекс: 2')#выводим на экран индекс 2
else:
    print('Нет ни одного равного числа индекс: 0')# Иначе вывод индекса 0
