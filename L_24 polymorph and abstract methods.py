# Полиморфизм это возможность работы с совершенно разными объектами
# языка Питон единым образом
class Geom:
    def get_pr(self):
        raise NotImplementedError('В дочернем классе должен быть переопределен метод get_pr()')
        #тогда мы будем знать что и где и как
        #методы которые обязательно нужно переопределять в дочерних классах и которые не имеют своей
        # собственной реализации называются абстрактными. чисто абстратных методов в питоне нету. это лишь имитация
class Rectangle(Geom):
    def __init__(self, w, h):
        self.w  = w
        self.h = h

    #def get_rect_pr(self):
        #return 2*(self.w+self.h)
    #def get_pr(self):  #допустим мы забыли
        #return 2 * (self.w + self.h)

class Square:
    def __init__(self, a):
        self.a = a

    #def get_sq_pr(self):
        #return 4*self.a

    def get_pr(self):
        return 4 * self.a
class Triangle:
    def __init__(self, a ,b ,c):
        self.a = a
        self.b = b
        self.c = c

    #def get_tr_pr(self):
        #return self.a + self.b + self.c

    def get_pr(self):
        return self.a + self.b + self.c

r1 = Rectangle(1,2)
r2 = Rectangle(3,4)

s1 = Square(10)
s2 = Square(20)

t1 = Triangle(1, 2 ,3)
t2 = Triangle(4, 5, 6)




#print(r1.get_rect_pr(), r2.get_rect_pr())
#print(s1.get_sq_pr(), s1.get_sq_pr())

geom = [
        Rectangle(1,2), Rectangle(3,4),
        Square(10), Square(20),
        Triangle(1, 2 ,3), Triangle(4, 5, 6)
        ]

for g in geom:
    print(g.get_pr())
    # И ВОТ ТЕПЕРЬ ОБРАЩАЕМСЯ  ЧЕРЕЗ ЕДИНЫЙ ИНТЕРФЕЙС
    # В этом и есть полиморфизм!

    #if isinstance(g, Rectangle):
        #print(g.get_rect_pr())
    #else:
        #print(g.get_sq_pr())

# давайте так . в каждом классе, метод который будет возвращать
# Периметр будет называться единым образом


#  что если мы забыли сделать метод для какого-то из классов?
# тогда создаем базовый класс который бы все это делал. а остальные классы уже наследуют его
# ну и это неправильно поэтому надо сделаь так raise NotimplementedError ( в дочеренм классе должен быть переопределен метод get_pr)
