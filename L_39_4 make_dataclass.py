from dataclasses import dataclass,field, InitVar, make_dataclass
from typing import Any

'''Функция make_dataclass'''
'''make_dataclass(cls_name, *, bases=(), namespace= None, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen = False
match_args=True,kw_only=False, slots=False, weakref_slot=False

cls_name = название нового класса в виде строки
fields = поля (локальные атрибуты ) объектов класса
* - произвольный набор позиционных аргументов
bases = список базовых классов
namespace = словарь для определния атрибутов самого класса, например так можно объявляеть методы класса
'''


''' Данную функцию используют если нужно сформировать класс в процессе работы программы, если же нам нужно обычное объявление
то удобнее использоватть датакласс'''

class Car:
    def __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed


CarData = make_dataclass('CarData', [('model', str),
                                     'max_speed',
                                     ('price', float, field(default=0))],
                         namespace={'get_max_speed': lambda self: self.max_speed})




c = CarData('BMW', 256, 4096)
print(c)
print(c.get_max_speed())
