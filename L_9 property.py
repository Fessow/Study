class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old
    '''чтобы не было дублирование функции сделаем декоратор property'''
    '''Мы расширили нашу функцию с помощью функции проперти'''
    @property
    def old(self): #get_old
        return self.__old

    @old.setter
    def old(self, old): #get_old
        self.__old = old

    # мы расширили нашу функцию с помощью гет олд которая расширина уже проперти
    # def set_old(self, old): НО ПИСАТЬ SET_OLD уже нельзя. ИМЕНА МЕТОДОВ ДОЛЖНЫ СОВПАДАТЬ когда используем декораторы

    #old = property(get_old, set_old) #ПО ПРИОРИТЕТАМ ЕМУ ОТДАЕТСЯ НАИВЫСШИЙ
    '''в результате мы через один атрибут класса old можем считывать данные с приватного св-ва или записывать данные
    в это же приватное св-во, нам не нужно запоминать геттеры и сеттеры. только old 
    вот для этого нужен property'''

    #у нас получилось правда дублирование
    # функции, надо сделать один единый интерфейс

    #old = property()
    #old = old.setter(set_old)
    #old = old.getter(get_old)

    @old.deleter
    def old(self):
        del self.__old

p = Person('Даниэль',28)
#p.set_old(29)
#print(p.get_old())


#все сработало, но есть проблема, нам надо прописывать геттер и сеттер
# для разных приватных аттрибутов
# как упростить? с помощью property

'''Если написать не old . a weight то это св-во появится '''
''''''
print(p.old)

p.old = 35
print(p.old)
del p.old

