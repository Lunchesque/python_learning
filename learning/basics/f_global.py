x = 50

def func():
    global x

    print('х равно', x)
    x = 2
    print('Змена глобального значения х на:', x)

func()

print('Значение х составляет', x)
