zoo = ('питон', 'слон', 'пингвин')      #zoo - кортеж элементов(последовательность), скобки, при создании кортеджа необязательны
print('Количество живности в зоопарке:', len(zoo))

new_zoo = 'обезьяна', 'верблюд', zoo    #new_zoo - кортеж с элементами, написанными руками и всеми элементами из кортежа zoo
                                        #кортеж внутри кортежа является отдельным элементом
print('Количество клеток в зоопарке', len(new_zoo))
print('Все животные в новом зоопарке:', new_zoo)
print('Животные привезенные из старого зоопарка:', new_zoo[2])  #new_zoo[2] - доступ к третьему элементу, кортежу zoo, в кортеже new_zoo
print('Последнее животное, привезенное из старого зоопарка:', new_zoo[2][2])    #new_zoo[2][2] - доступ к третьему элементу(кортежу zoo)
                                                                                #в котреже new_zoo и третьему элементу третьего элемента
                                                                                #(кортежа zoo)
print('Количестео живатных в новом зоопарке:', len(new_zoo) - 1 + len(new_zoo[2]))