# attribute без одного или двух подеркиваний - публичное свойство

#_attribute -  одним подчеркиванием - protected (служит для обращения внутри класса и во всех дочерних классах)

#__attribute -  двумя подчеркиваниями - private служит для обращения только внутри класса

class Geom:
    __name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'Инициализатор класса для{self.__class__}')
        self._verify_coord(x1)
        self._x1 = x1 # по логике два подчеркивания написаны правильно в родительском классе
        self._y1 = y2 # но если надо чтобы было и в дочерних. сделаем одно подчеркивание
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name

    def _verify_coord(self, coord):
        return 0<= coord < 100

#class Line(Geom):
    #def __init__(self, x1, y1, x2, y2, fill = 'red'):
        #super().__init__(x1, y1, x2, y2)
        #self.__fill = fill


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill = 'red'):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill
        self._verify_coord(x1)
        #self.__verify_coord(x1)  !ОШИББКА НЕЛЬЗЯ
        #self.__name == Geom.__name         !нельзя. ошибка. файл private
    def get_coords(self):
        return (self._x1, self._y1)

r = Rect(1, 2, 3 , 4)

print(r.__dict__) #Перед всеми свойствами добавляется префикс класса
# не смотря на то что параметр селф является ссылкой на объект класса рект.
# это особенность . В ТОМ КЛАССЕ ГДЕ ПРОПИСАНЫ __ , тот префикс и добавляется
# следовательно нельзя обратится к этим атрбитам через дочерний класс!!!!

r.get_coords() # ДАСТ ОШИБКУ ПОТОМУ ЧТО _Rect__x1 НЕТУ В ДОЧЕРНЕМ КЛАССЕ

print(r._x1) # опять получается доступно извне но обращаться так не следует

# те же ограничения доступа можно применять и на методы ( функции)