#Можно использовать собственные метаклассы

##class Point:
    ##MAX_COORD = 100
    ##MIN_COORD = 0

# сделаем класс -как выше, через ФУнкцию. да можно сделать функцию класс

#def create_class_point(name, base, attrs):
    #attrs.update({'MAX_COORD':100, 'MIN_COORD': 0}) #словарь атрибутов
    #return type(name, base, attrs)

class Meta(type):
    def __new__(cls, name, base, attrs): # метод new вызывается непосредственно перед созданием класса
        attrs.update({'MAX_COORD':100, 'MIN_COORD': 0}) # класс еще не создан, и мы тут только будем его создавать поэтому нужна эта строчка
        return type.__new__(cls, name, base, attrs)
    #def __init__(cls, name, base , attrs):
        #super().__init__(name, base, attrs) # это тоже надо
        #cls.MAX_COORD = 100 #класс уже создан поэтому мы в новый созданный класс динамически добавляем два атрибута
        #cls.MIN_COORD = 0


#class Point(metaclass=create_class_point): #когда отрабатывает функция create ,то питон автоматически передает имя Point , далее кортеж из базовых классов, он тут пустой, а затем атрибуты
class Point(metaclass=Meta):
    def get_coords(self):
        return (0,0)

# это учебный пример скорее, на практике не используется

pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())