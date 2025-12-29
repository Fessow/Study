#__iter(self) - получение итератора для перебора объекта
# __next__(self) - переход к следующему значениюм и его считывание

# любой список это итерируемый объект поэтому для него можно создать итератор.
# это некий интерфейс для перебора элементов лююбого итерирового объекта затем
# мы вызвыаем некст и последовательно читаем элемент объекта
# range (start, stop , step) - арифметическая последовательность

b = list(range(5))

a = iter(range(5))

#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))

class FRange:
    def __init__(self, start = 0.0, stop = 0.0, step = 1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step #счетчики то с нуля
    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

fr = FRange(0, 2 , 0.5)
#print(fr.__next__()) = print(next(fr)) эквиваленты
#print(fr.__next__())
#print(next(fr))

# в качестве итератора выступает сам объект FRange
# Итератор это некий объект у которого есть магический метод некст
# и вывает этот магический метод некст функция некст

print(fr.__next__())
print(next(fr))

for i in fr:
    print(i)
# но наш объект не итерируемый , потомучто мы не можем создрать итератор
# не можем вызвать функцию iter к нашему объекту

#it = iter(fr0)
# ПОЭТОМУ НАДО СОЗДАТЬ ВТОРОЙ МАГИЧЕСКИЙ МЕТОД ПОД НАЗВАНИЕМ ИТЕР


class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows =5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    #два вложенных цикла for
    def __iter__(self):
        self.value = 0
        return self

    def __next__(self): # возвращает итератор который будет вовзращать числовые значения
        if self.value < self.rows: # мы не прошли все нужные нам строки
            self.value += 1   # тогда мы будем генерировать эти строки
            return iter(self.fr)
        else:
            raise  StopIteration


fr = FRange2D(0, 2, 0.5, 4)
print('xxxxxxxxxxxxxxxx')
for row in fr:
    for x in row:
        print(x, end =' ')
    print()