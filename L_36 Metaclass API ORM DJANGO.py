''' Джанго использует метаклассы для связи обхектов в записями в базе данных
Он делает следующее --- можно определить некий класс модели, с набором атрибутов, причем
 эти атрибуты совпадают с соотвествующими полями в табилце БАЗЫ ДАННЫХ

в объекте добавляются локальные свойства , что и у атрибута класса, но эти локальные свойства буду содержать конкретные данные
Class Women(models.Model): вот этот базовый класс Model является Метаклассом , добавляя необходимый фукнционал в класс модели Women

 '''

#сделаем свой метакласс
class Meta(type):
    def create_local_attrs(self, *args, **kwargs): # Этот метод будет инициализатором класса women
        #Формируем локальные свойства объекта women
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, bases, attrs):
        cls.class_attrs = attrs #словарь атрс
        cls.__init__ = Meta.create_local_attrs # ссылка на функцию

class Women(metaclass=Meta):
    title = 'заголовок'
    content = 'контент'
    photo = 'путь к фото'

w = Women()
print(w.__dict__) #Логика формирования локальный св-в вынесена в мета класс, и в


# ПО сути Метакласс превращает класс women в класс вот такой

class Woman: # специально написал через А чтобы увидели разницу
    class_attrs = {'title': 'заголовок', 'content':'контент','photo':'путь к фото'}
    title = 'заголовок'
    content = 'контент'
    photo = 'путь к фото'

    def __init__(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

w = Woman()
print(w.__dict__)

# По сути одинаково, это все нужно для Django . API ORM DJANGO
