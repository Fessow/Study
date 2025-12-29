class Geom: # class Geom(object): c питоне 3 ээто делается автоматически
    pass

class Line(Geom):
    pass


#Наследование object <---- Geom <---- Line
g = Geom()
l = Line()
print(g)
print(Geom.__name__)
print(l.__class__)
print(issubclass(Line, Geom)) #работает функция только с классами, но не с экземплярами
print(issubclass(Geom, Line))  #работает функция только с классами, но не с экземплярами
print('---------')
print(isinstance(l, object)) #работает функция с объектами этих классов
print(isinstance(Geom, object)) #работает функция с объектами этих классов

#Классы int, float, list, dict, tuple,set
print('---------')
print(issubclass(int, object))
print(issubclass(list, object))
print('---------')
print('---------')
print('---------')
class Vector(list):
    def __str__(self):
        return " ".join(map(str, self)) #где селф это список

v = Vector([1, 2, 3])
print(v)
print(type(v))