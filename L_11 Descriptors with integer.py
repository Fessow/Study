#Работаем с локальными свойствами класса поинт через вот эти интерфейсы интежер
#можно создать ,сколько хочешь x y z a b c и т.д.
#этот класс представляет собой дескриптор данных.
# дескриптор не данных не имеет сеттера или делитера
class ReadIntX: # дескриптор неданных
    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

class Integer: # дескриптор данных
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координата должна быть целым числом')

    def __set_name__(self, owner, name):

        self.name = '_' + name

    def __get__(self, instance, owner):
        # обращеие к локальным свойствам экземпляра класса через функции гет и сет
        return getattr(instance, self.name) # так правильно
        #return instance.__dict__[self.name] так не совсем правильно

    def __set__(self, instance, value):

        #print(f'__set__: {self.name} = {value}')
        # обращеие к локальным свойствам экземпляра класса через функции гет и сет
        self.verify_coord(value)
        setattr(instance, self.name, value) # так правильно
        #instance.__dict__[self.name] = value так не совсем правильно

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1,2,3)
p.xr = 5 # создали локальный атрибут и присвоили значение 5  с помощью дескриптера неданных

print(p.xr, p.__dict__)

# Приоритет у дескрипторов разный, если бы задали сеттер в дескриптере неданных, наше значение 5
# которое появляется в принте до словаря, имело бы значение единицу.



