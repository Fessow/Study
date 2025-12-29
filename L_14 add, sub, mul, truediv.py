

# магические методы
# __add__ - операция сложение + idd
# __sub__ - операция вычитания - isub
# __mul__ - операция умножения  * imul
# __truediv__ - операция деления itruediv x/y
# __floordiv__ - операция деления без остатка ifooldiv x//y
# __mod__ - операция остатка imod x%y

class Clock:
    __DAY = 86400

    def __init__(self, seconds : int): # указывает программисту что надо указывать целые число но по прежнему можно вбить и строку
        if not isinstance(seconds, int):
            raise ValueError('Sekundi doljni bit celim chislom')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600 ) % 24
        return f'{self.__get_formatted(h)} : {self.__get_formatted(m)} : {self.__get_formatted(s)}'

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый оперант должен быть инт')

        sc = other # если целое число то ссылает на целое число
        if isinstance(other, Clock): # а если клок, то будет ссылаться на св-во секондс объекта other
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other): # чтобы не было ошибки когда экземпляр справа а число слева
        return self + other

    def __iadd__(self, other):
        print('__iadd__')
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Praviy operand doljen bit chislom')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += sc
        return self

c1 = Clock(1000)
# допустим мы хотим теперь увеличить время на какоето количество секунд
c1.seconds = c1.seconds + 100

# но хотелось бы чтобы можно было записывать проще
c1 = c1 + 100
# ошибка
print(c1.get_time())

c2 = Clock(2000)

c3 = Clock(3000)

c4 = c1 + c2 + c3

c5  = 100 + c1 # budet oshibka

c5 += 100

print(c4.get_time())

