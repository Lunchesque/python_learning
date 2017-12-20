number = 23
running = True

while running:
    guess = int(input('Введите целое число:'))

    if guess == number:
        print('Вы угадали')
        running = False
    elif guess < number:
        print('Загаданное число больше, чем то, что вы ввели.')
    else:
        print('Загаданное число меньше, чем то, что вы ввели.')

print('Конец')
