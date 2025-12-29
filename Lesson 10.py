import numpy as np


a = np.array([ 1,  2,  3, 10, 20, 30])

print(a.sum())
print(a.mean())
print(a.max())
print(a.mean())

a.resize(3,2)
print(a)

print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))

print(a.max(axis=0))
print(a.min(axis=1))

a = np.array([-1, 1, 5, -44, 32, 2])

print(np.abs(a)) # array([ 1,  1,  5, 44, 32,  2])
print(np.abs(-10.5))
print(np.abs([-1, 1, 5, -44, 32, ]))# array([ 1,  1,  5, 44, 32]
print(np.round(-0.6))
print(np.log(a)) # array([nan, 0. , 1.60943791,  nan, 3.4657359,0.69314718])
print(np.argmax(a))
print(np.argmin(1))
a.resize(2, 3)
print(np.argmax(a, axis=0))  # array([-1, 32,  5])
print(np.argmax(a, axis=1)) # array([2, 1], dtype=int32)

a = np.linspace(0, np.pi, 10)
res1 = np.sin(a) # возвращает массив синусов углов
print('aaaaa')
print(a)
print(res1)
print(np.sin(np.pi/3))
print(np.cos([0, 1.57, 3.17]))
res2 = np.cos(a) # возвращает массив косинусов углов
np.arcsin(res1) # возвращает арксинусы от значений res1