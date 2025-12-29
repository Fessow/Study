class Point2D:
    __slots__ = ('x', 'y', '__lenght')  # Не накладывает ограничения на аттрибуты самого класса

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__lenght = (x * x + y * y)**0.5 # длина радиус вектора

    #через декоратор property мы можем прописать то или  иное свойство
    @property
    def lenght(self): # Это аттрибут класса ПОИНТ2Д, а не локальное св-во
        return self.__lenght

    @lenght.setter
    def lenght(self, value):
        self.__lenght = value

pt = Point2D(1,2) # свойство lenght появилось автоматически
print(pt.lenght)
pt.lenght = 10
print()
# что если написать прописать свойство с тем же самым именем lenght
#


class Point2D2:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point2D2):
    #pass
    __slots__ =  'z', #__slots__ = () # ТЕПЕРЬ ЕСТЬ ОГРАНИЧЕНИЕ . ДОСТУПНЫ ТОЛЬКО X и У  ( если пусто)

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

pt3 = Point3D(10, 20)
pt3.z = 30 # ВАЖНО!!!
# КЛАСС ПОИНТ3Д НЕ НАСЛЕДУЕТ КОЛЛЕКЦИЮ __slots__ и здесь мы можем создавать самые разные локальные св-ва
# и вот у класса 3д есть __dict__ но х и у из point2d сюда не попадают

#print(pt3.__dict__)
print(pt3.x)
del pt3.x
pt3.x = 20
#print(pt3.__dict__)

# ВЫВОД если в классе поинт3д мы пропишем коллекцию слотс пустой. но значит в нем будет разрешены только х и у


