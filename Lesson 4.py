import numpy as np

a = np.arange(10)
print(a)
a.shape = 2,5

print(a)

b = a.reshape(10)
print(b)

b[0]=-1
print(a)
print(b)

#два разных представления но данные одни и те же!
#всегда работают с полным набором данных

#b = a.reshape(9) - ошибка, так делать нельзя. у нас 10 элементов и со всеми 10 надо работать

#a.shape = 3, 3 - ошибка, так делать нельзя, так как у нас 10 элементов

a.shape = -1, 2
print(a)

a.shape = -1, 5
print(a)

print(b.reshape(-1,1))

print(b.reshape(1, -1))

c = a.ravel()
print(c)

a.shape = -1
print(a)

a.resize(2, 5)
print(a)

#a.resize(3, 3) - ошибка но можно сделать по другому

a.resize(3, 3, refcheck=False)
print(a)

a.resize(4, 5, refcheck=False)
print(a)

#транспонирование. новый массив не создается. данные те же.
a = np.array([(1,2,3), (1,4,9), (1,8,27)])
b = a.T
print(b)

x = np.arange(1,10)
z =x.T
#не получится так как вектор. одна строка и все. чтобы применить операцию нам нужно добавить одну ось

x.shape = 1,-1
z = x.T
print(z)

