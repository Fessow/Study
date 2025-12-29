# len () вызывается функцией bool() если не определен маг метод bool()
# bool взывается в приоритетном порядке функцией bool

# bool('') = False bool(123) = True
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__00')
        return self.x * self.x + self.y * self.y

    def __bool__(self): #работает в приоритете и обязательно должен возвращать только булевые значения
        print('bool')
        return self.x == self.y

p = Point(3, 4)
print(len(p))
print(bool(p))

p2= Point(0, 0)
print(len(p2))
print(bool(p2))

p3 = Point(10,10)
print(bool(p3))