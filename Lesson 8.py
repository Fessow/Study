import numpy as np

lst = [1,2,3]
a = np.array([1,2,3])

print(lst * 2)# список: [1, 2, 3, 1, 2, 3]
print(a * 2) # массив: array([2, 4, 6])

print([x*2 for x in lst])

print(-a) # унарный минус
print(a + 2) # сложение с числом
print(2 + a)  # так тоже можно записывать
print(a - 3)# вычитание с числом
print(a * 5)# умножение на число
print(a / 5)  # деление на число
print(a // 2)  # целочисленное деление
print(a ** 3)  # возведение в степень 3
print(a % 2)  # вычисление по модулю 2
print('------------')
b = np.array([3, 4, 5])

print(a - b)  # array([-2, -2, -2])
print(b + a)  # array([4, 6, 8])
print(a * b)  # array([ 3,  8, 15])
print(b / a)  # array([3. , 2. , 1.66666667])
print(b // a) # array([3, 2, 1], dtype=int32)
print(b ** a) # array([  3,  16, 125], dtype=int32)
print(b % a)  # array([0, 0, 2], dtype=int32)

#Массивы должны быть одного размера!!

b = np.array([3, 4, 5, 6])
#a + b  # ошибка: длины массивов не совпадают

b = np.arange(1, 7)
b.resize(2, 3)
print(a + b)
# транслоирование массивов




a = np.arange(1, 19)
a.resize(3, 3, 2)
b = np.ones((3, 2))

print(a - b)
print(a * 10)
print(a // b)