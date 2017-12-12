print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist   #mylist - еще одно имя указывающее на тот же объект что shoplist

del shoplist[0]     #удаление первого элемента из списка

print('shoplist:', shoplist)    #вывод shoplist
print('mylist:', mylist)        #вывод mylist
#оба вывода выводя одинаково, список без яблок

print('Копирование при помощи полного среза:')
mylist = shoplist[ : ]
del mylist[0]

print('shoplist:', shoplist)
print('mylist:', mylist)
#тепеперь списки разные потому что mylist указывает на список-срез всех элементов shoplist, поэтому удаляя теперь элементы из mylist,
#удаляются элементы из полного среза, а не из списка shoplist
