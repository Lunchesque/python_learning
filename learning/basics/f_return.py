def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны'
    else:
        return y
print(maximum(int(input('Введите первое число:')), int(input('Введите второе число:'))))
