#!/usr/bin/python3
#-*- coding: utf-8 -*-
#fdsfdsfklsdhfls

class Robot:

    population = 0      #приадлежит классу Robot, переменная класса, вызов этой переменной осуществляется всегда через
                        #Robot.population(class.varieble)
    def __init__(self, name):
        self.name = name    #переменная name принадлежит объекту, прискаивание значение происходит через self, вызов этой
                            #пеерменной высегда осуществляется через self.name
        print('(Инициялизация {0})'.format(self.name))
        Robot.population += 1

    def __del__(self):  #запускается только тогда, когда объект перестает использоваться, а поэтому заранее неизвестно,КОГДА
        print('{0} уничтожение'.format(self.name))  #этот момент наступит, поэтому чтобы увидеть его явно, использовался
        Robot.population -= 1                       #оператор del

        if Robot.population == 0:
            print('{0} был последним'.format(self.name))
        else:
            print('Осталось {} работающих роботов'.format(Robot.population))

    def sayHi(self):
        print('Hi, im {0}'.format(self.name))

    def howMany():  #этот метод можно определить как classmethod - для информации о принодлежности к классу
        print('У нас {} роботов'.format(Robot.population))  #или staticmethod - елси информация о принадлежности к методу
                                                            #не нужна
    howMany = staticmethod(howMany)

droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()
droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

print("\nРабота для роботов\n")

print("пора уничтожить роботов")
del droid1
del droid2

Robot.howMany()
