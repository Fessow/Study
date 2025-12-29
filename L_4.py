class Point:
    ''' Иногда нужно что-то сделать ДО создания объекта'''
    '''реализация метода СИНГЛЕТОН делается через метод new'''
    '''Т.к все классы наследуются от object и из этого базового класса мы и вызываем метод __new___'''
    def __new__(cls, *args, **kwargs):
        print(str(cls)) #CLS ссылается на сам класс
        return super().__new__(cls)
        # КОГДА мы вызываем функцию super в этом классе поинт то получаем ссылку на базовый класс, и в этом базовом классе через эту ссылку мы вызвыаем метод new
        # и этот метод new запускает процесс создания класса и возвращает адресс нового созданного объекта
        # а мы вовзращаем этот адрес дальше


    def __init__(self, x=0, y=0):
        print(str(self))
        self.x = x
        self.y = y

pt = Point(1,2) #в данный момент экземпляр класса не был создан
print(pt) #будет none

'''Почему? потому что метод new должен возвращать адресс объекта'''


'''ПАТТЕРН синглетон это когда у нас может существовать ТОЛЬКО ОДИН экземпляр класса и ВВСЕ, ВТОРОЙ СОЗДАВАТЬСЯ НЕ ДОЛЖЕН'''


class DataBase:
    __instance = None # вот это будет ссылкой на экземпляр класса, если его нету то будет none
    #а если будет , то будет ссылка на этот экземпляр
    # таким образом мы можем контролировать существует или нет экземпляр

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'соединение с БД{self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Zakrili')

    def read(self):
        return 'data s bd'

    def write(self, data):
        print(f'запись{data}')



db = DataBase('root', '1234', 90)
db2 = DataBase('root2', '15345', 32)

print(id(db), id(db2))
'''как видим второй экземпляр не создался'''

db

