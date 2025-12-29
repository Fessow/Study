'''__setattr__(self,key,value) - автоматически вызывается при изменении свойства key класса

__getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item

__getattr ( self, item)  автоматически вызвается при получении несуществующего св-ва item класса

__delattr__(self, item) - автоматически вызывается при удалении свойства item (не важно существует оно или нет)

'''

class Point:

    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x= 0, y=0):
        self.__x = x
        self.__y = y

    def set_coord(self,x ,y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        '''запрет к обращению к атрибуту'''
        print('_get_attribute_')
        if item == 'x':
            raise ValueError('доступ запрещен')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        '''запрет на создание какого-либо локального атрибута, например атрибут z '''
        print('_setattr_')
        if key == 'z':
            raise AttributeError('недопустимое имя атрибута')
        else:
            return object.__setattr__(self, key, value)
            self.__dict__[key] = value

    def __getattr__(self, item):
        '''если идет обращение к несущ атрибуту лучше возвращать False'''
        return False
        #print('__get__atr' + item)
    '''чтобы не было ошибок '''

    def __delattr__(self, item):
        print('__delattr' + item)
        return object.__delattr__(self, item)

pt1 = Point(1,2)
#a = pt1.x # как только идет обращение к атрибуту - срабатывает этот метод
#print(pt1.yy)
#del pt1.x
print(pt1.__dict__)