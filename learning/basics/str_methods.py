name = 'Swaroop'  #строка - объект типа str

if name.startswith('Swa'):  #метод startswith определяет, начинается ли строка с заданной подстроки
    print('Да, эта строка начинается на "Swa"')

if 'a' in name:     #оператор in используется для определения, находится ли заданная подстрока в проверяемой
    print('Да, эта строка содержит подстроку "a"')

if name.find('war') != -1:      #метод find используется для определения позиции заданной подстроки в строке, find возвращает -1 если
    print('Да, эта строка содержит "war"')      #строка не обнаружена

delimiter = '_*_ '
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print('''delimiter''''_*_ '.join(mylist))       #метод join объединяет елементы последовательности с указанной строкаой в качестве разделителя между
                                    #элементами, возвращает большую строку сформированную таким образом
