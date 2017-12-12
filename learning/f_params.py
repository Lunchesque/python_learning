def printMax(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print('{} равно {}'.format(a, b))
    else:
        print(b, 'максимально')

printMax(3, 4)

x = 5
y = 7

printMax(x, y)
