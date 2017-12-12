class SchoolMember:
    #этот класс будет представлять любого человека в школе
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))
    def tell(self):
        #вывод информауии
        print('Имя: "{0}" Возраст "{1}"'.format(self.name, self.age), end=' ')
class Tearher(SchoolMember):
    #этот класс представляет преподавателей
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Tearher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    #пердставляет студента
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))

        def tell(self):
            SchoolMember.tell(slef)
            print('Оценки: "{0:d}"'.format(self.marks))



t = Tearher('Shrividya', 40, 30000)     #создание экземпляра класса Tearher
s = Student('Swaroop', 25, 75)      #создание экземпляра класса Student
s = Student('Serg', 24, 84)

print()     #печать пустой строки для отступа

members = [t, s]

for member in members:
    member.tell()
