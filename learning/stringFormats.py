age = 26
name = 'Swaroop'

print('Age {} -- {} years.'.format(name, age))      #использование {} куда удобнее склеивания строк
print('Why Python playing with {}?'.format(name))   #в {} записываются переменные, указанные в методе format
print('{0:.10}'.format(1/3))    #{0:.10} - число 10 указывает точность(количество выводимых знаков после запятой) результата деления в методе format
print('{0:_^11}'.format('hello'))   #строка с длинной в 11 символов, текст, указанный в методе format, центрирется, остальное заполняется символами "_"
print('{name} написал {book}'.format(name='Gendalf', book='A Byte of Python'))  #{name}, где name - ключевое слово, описанное в методе format
