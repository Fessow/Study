class Point:
    'Класс для представления координат точек на плоскости'
    color = 'red'
    circle = 2

a = Point()
b = Point()

Point.deep = 0.5

print(Point.__dict__)

#setatttr(Point, 'prop', 1)

#getattr(Point, 'a', False)
#getattr(Point, 'color', False)

if hasattr(Point, 'deep'):
    del Point.deep

print(Point.__dict__)

if hasattr(Point, 'circle'):
    delattr(Point, 'circle')

print(Point.__dict__)
print(Point.__doc__)

if hasattr(a, 'color'):
    del a.color # после удаления в объекте атрибута, он стал браться из класса Point
    print(a.__dict__)

