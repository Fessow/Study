# каждый магический метод срабатывает в определенный момент времени

# 1. __STR__() для отображения информации об объекте класса для пользователей ( например принт или стр)
# 2. __REPR__() для отображения информации об объекте класса в режиме отладки ( для разработчиков)
# 3. __len__() позволяет применять функцию len() в экземплярам класса
# 4. __abs__() позволяет применять функцию abs() к экземплярам класса


class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f'{self.name}'


class Point:
    def __init__(self, *args):
        self.__coords = args  #spisok iz tochek

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))

p = Point(1,-2)
print(len(p))
print(abs(p))



