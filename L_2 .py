class Point:

# Имена методов в классах это те же самые атрибуты , просто они ведут не на данные
#а на функции

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

pt = Point()
pt.set_coords(1, 4)

print(pt.__dict__)

pt2 = Point()
pt2.set_coords(1,6)
print(pt2.get_coords)
f = getattr(pt2,'get_coords')
print(f())

