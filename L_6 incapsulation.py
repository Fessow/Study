from accessify import private, protected  #ЭТА ЗАЩИТА ЛУЧШЕ ЧЕМ ПОДЧЕРКИВАНИЯ

'''attribute - public '''
'''_attribute  - режим доступа Protected (служит для обращения внутри класса и в дочерних классах'''
'''__attribute - режим доступа Private - (служит для образения внутри класса)'''

#Protected  ЛИШЬ Сигнализирует о том, что данное св-во является защищенным, но никак явно не ограничивает доступ к нему извне.
#Оно предостерегеает программиста от использования вне класса
# впоследствие это может стать проблемой. никто не предполагал доступка к нему извне.

# Protected - внутренняя служебная переменная


#Private - внутри классса можно обращаться, извне нет
#


class Point:
    def __init__(self, x= 0, y=0):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
    @private
    @classmethod
    def check_value(cls, x): #приватный метод __check_value(cls, x)
        return type(x) in (int, float)


    def set_coord(self, x, y):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('координаты должны быть цифрами')

    def get_coord(self):
        return self.__x, self.__y


'''интерфейсные методы - сеттер и геттер 

стобы не нарушить целостность алгоритма и класса следует взаимодействовать с ним только через публичные методы и св-ва
в этом суть принципа инкапсуляции вот для этого надо обращаться только через сеттеры и геттеры

с помощью них можно и проверять правильность '''
pt = Point(1,2)
#print(pt.__x, pt.__y)
pt.set_coord(10,15)
print(pt.get_coord())

print(dir(pt))