# __eq__ - равенство ==
# __ne__ - неравенство !=
# __it__ - равенство <
# __le__ - неравенство <=
# __gt__ - равенство >
# __ge_ - неравенство >=

class Clock:
    __DAY = 86400

    def __init__(self, seconds : int): # указывает программисту что надо указывать целые число но по прежнему можно вбить и строку
        if not isinstance(seconds, int):
            raise ValueError('Sekundi doljni bit celim chislom')
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls,other):
        if not isinstance(other, (int, Clock)):
            raise TypeError ('operand sprava doljen bit int ili clock')

        return other if isinstance(other, int) else other.seconds


    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

        # ПИТОН делает так - когда видит с1 ! = с2 он использует not(c1==c2)

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc
    # код потворяется. чтобы такого не было сделаем метод уровня класса выше @classmethod
    # ПИТОН делает так - когда видит с1 > с2 он использует он проверяет так c2 < c1

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc

    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds > sc

    def __ge__(self, other):
        sc = self.__verify_data(other)
        return self.seconds >= sc


c1 = Clock(1000)
c2 = Clock(1000)

print(c1 >= c2)