from dataclasses import dataclass,field, InitVar
from typing import Any

class GoodsMethodsFactory: # вспомогательный класс для габаритов
    @staticmethod
    def get_init_measure():
        return [0,0,0]


@dataclass
class Goods:
    # def __init__(uid: Any, price: Any = None, weight: Any = None):
    '''формируем значения UID автоматически при создания новго объекта'''
    current_uid = 0 # параметр будет существовать в классе, но пропускаться декоратором датакласс, декоратор его никак не заметит

    uid: int = field(init=False) #исключили из инициализатора
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print('Goods: post_init')
        Goods.current_uid+=1
        self.uid = Goods.current_uid
    # Теперь айдишник формируется автоматически для каждого нового объекта

@dataclass
class Book(Goods):
    # def __init__(self,uid: Any, price: float = 0, weight: int or float = 0, title: str='', author: str=''):
    title: str = "" #4 атрибут
    author: str = "" #5 атрибут
    price: float = 0  #2 атрибут
    weight: int or float = 0 #3 атрибут

    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure) # габариты книги

    #@staticmethod
    #def get_init_measure():
        #return [0, 0, 0]
    #не будет работать не будет

    #def __post_init__(self): # будет ошибка,  потому что сначала ищет self.post_init() в дочеренем классе, потом ищет в базовом классе
        # у нас он нашел в дочернем классе , а в базовом он был вызван, поэтому локальное св-во uid не сформировалось
        # как исправить?
        #print('Book: post_init')

    def __post_init__(self):
        super().__post_init__() # делаем через super . __init__ закладывать не надо, т.к. у нас есть декоратор
        print('Book: post_init')


b = Book(1000, 24, 'python 10', 'шрек шрекович')
print(b)

a = Book(1000, 24, 'python 10', 'шрек шрекович')
print(a)

