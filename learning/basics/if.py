number = 23
guess = int(input('Введите целое число: '))     #input записывает в переменную guess значение введенное с клавиатуры
                                                #int показывает значение какого класса будет введено, в данном случает integer,
                                                #если не указывать тип, то по умолчанию Python будет думать, что введена строка

if guess == number:             # == оператор сравнения, означет что одно равно другому
    print('Поздравляю, Вы угадали.')    #начало блока
    print('Но приза не ждите, не туда попали...')   #конец блока
elif guess < number:
    print('Загаданное число больше, чем то, что Вы ввели.')     #начало еще одного блока
                                                                #внутри блока может быть множество операций
else:
    print('Загаданное число больше, чем то, что Вы ввели.')

print('Конец')  #индикатор завершения выполнения программы