def printMax(x, y):
    '''Выводит максимальное значение.
    
2х введнных с клавиатуры чисел'''

    if x > y:
        print(x, 'больше', y)
    else:
        print(y, 'больше', x)
print(printMax.__doc__)
printMax(int(input('Введите первое число:')), int(input('Введите второе число:')))
