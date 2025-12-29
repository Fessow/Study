'''атрибуты класса являются общиими для всех экземпляров'''

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

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

    '''def set_bound(self, left):
        self.MIN_COORD = left # оператор присваивания создает атрибут в локальной области видимости т.е внутри экземпляра класса
    #Поэтому так писать неправильно'''

'''Нам нужен метод который бы изменял значение МИН_КООРД'''


pt1 = Point(1,2)
pt1.set_bound(-100)
print(pt1.__dict__)
print(Point.__dict__)




