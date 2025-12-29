from string import ascii_letters

class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old , ps, weight):
        self.verify_fio(fio)
        #self.verify_old(old)
        #self.verify_ps(ps)
        #self.verify_weight(weight)
        # не обязательны ,т.к мы уже задали это и указали в сеттере

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

        # вспомогательные методы класса для проверка корректности введеных данных
    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')

        spisok_fio = fio.split()
        if len(spisok_fio)!= 3:
            raise TypeError('ФИО должно записываться через пробел')

            #проверка, что только буквенные символы и дефис в ФИО
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in spisok_fio:
            if len(s) < 1:
                raise TypeError('ФИО должен быть хотя бы один символ')
            if len(s.strip(letters)) !=0:
                raise TypeError('ФИО может быть только буквенные симоволы и дефис')

    @classmethod
    def verify_old(cls,old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('Возраст должен быть целым числом от 14 до 120')

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w<20:
            raise TypeError('Вес должен быть числом с плавающей точкой ( вещественным ) от 20 и выше')


    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('Паспорт должен быть строкой')
        spisok_ps = ps.split()
        if len(spisok_ps)!=2 or len(spisok_ps[0])!=4 or len(spisok_ps[1])!=6:
            raise TypeError('Неверный формат паспорта')

        for p in spisok_ps:
            if not p.isdigit():
                raise TypeError('Серия и номер паспорта должны быть числами')


    @property
    def fio(self):
        return self.__fio
    #Не задали сеттер, только геттер.

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old) # обязательно проверим на правильность данных
        self.__old = old
    #название - (олд) в геттере и сеттере должно совпадать
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight) #обязательно проверям правильность введенных данных в сеттере
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps



p=Person('Мирзабаев Даниэль Иноятович', 28, '1234 567890', 80.0)
p.old = 100
p.passport = '1234 123456'
p.weight = 70.0

print(p.__dict__)