i = 5   #присваивание переменной i значения 5
print(i)    #вывод переменной i
i = i + 1   #присваивание переменной i значение i + 1(5 + 1)
print(i)    #вывод переменной i с измененным значением, переменная i осталась со значением i + 1 (6)

s = '''Это многочтрочная строчка.
Это вторая строка.'''    #в трех одинарных кавычках можно записать строковую переменную в несколько строк с форматированием внутри кавычек
print(s)    #вывод переменной s

s = 'Это одна строка. \
Эта строка продолдается в одной строке.'    #символ "\" объединяет 2 физические строки в одну логическую(логическая строка - то как видит код Python)
print(s)

print\
(i)     #пример объединения двух физических строк в одну, такая запись аналогична print(i)