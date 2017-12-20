while True:
    s = input('Введите что-то: ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком короткое занчение')
        continue
    print('Строка нормальной длинны')
