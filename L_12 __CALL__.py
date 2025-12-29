import math


class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step = 1, *args, **kwargs):
        print('__call__')
        self.__counter += step
        return self.__counter

c=Counter()  # __Call__(self, *args, **kwargs):
            #   obj = self.__new__(self, *args, **kwargs)
            # self.__init__(obj, *args, **kwargs)
            # return obj
c2=Counter()

c()  # Если не прописать метод def __call__ будет ошибка. т.к экземпляр КЛАССА НЕ ВЫЗЫВАЕМ
# Если прописать уже __call__ то ошибок не будет и метод call сработал
# благодаря ему можем вызывать экземпляры класса подобно функциям и называются ФУНКТЕРЫ


c()
c()

res2 = c2(10)
res = c(5)
print(res, res2)

#изначально счетчик был равен 0 , а после 4 вызывов стал равен 4

#можно создать независимые счетчики, например с2 с3

#ГДЕ ИСПОЛЬЗУЮТСЯ?
# 1 . Замена замыканий функций
# 2. В классе декораторе

class StripChars: #Удаление символов в конце и вначале строки
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError ('ARGUMENT DOLJEN BIT STROKOY')

        return args[0].strip(self.__chars)


s1 = StripChars('!?@#!@#') # мы хотим удалить эти символы вначале и в конце строки

resultat = s1('Hello word!') # удаляем символы которые есть в переменной s1

s2 = StripChars(' ')

resultat2 = s2(' Hello word! ')
resultat3 = s1 ('@pes!')

print(resultat, resultat2, resultat3, sep='\n')


#Далее декоратор на уровне классов. МЫ пропишем декоратор который позволяет выычислять производные определенной функции в некой точке икс

class Derivate:
    def __init__(self, func ): # передаем функцию фукнционал которой будем расширять
        self.__fn = func


    def __call__(self, x, dx=0.0001, *args, **kwargs):
        #возвращаем результат вычисления производной функции
        return (self.__fn(x + dx) - self.__fn(x)) /dx

#функция для которой производная будет считаться
@Derivate
def df_sin(x):
    return math.sin(x)

print(df_sin(math.pi/4))

#df_sin = Derivate(df_sin) #Превратили функцию в экземпляр класса Деривате
# теперь эта переменная ссылается не на функцию а на экземпляр класса

print(df_sin(math.pi/3))