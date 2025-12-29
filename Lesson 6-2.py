import numpy as np

print(np.r_[ [1, 2, 3], 4, 5]) # список + дополнительные элементы
print(np.r_[ 1:9, 90, 100]) # срез + два элемента
print(np.r_[ np.array([1,2,3]), np.array([4,5,6])])# объединение двух массивов
print(np.r_[ [(1,2,3), (4,5,6)], [(7,8,9)] ]) # объединение двумерного и одномерного списков
print('--------------------')
print(np.c_[1:5])
print(np.c_[ [1, 2, 3], [4, 5, 6]])
print(np.c_[ [(1,2,3), (4,5,6)], [[7],[8]] ])
print('--------------------')
a = np.arange(10)

b = np.hsplit(a,2)
print(b)

#np.hsplit(a, 3) # ошибка 10 на 3 нацело не делится

#np.vsplit(a, 2) # ошибка: нет вертикальной оси

a.shape = 10, -1 # вектор-столбец
print(np.vsplit(a, 2))

a = np.arange(12)
a.resize(2, 6)  # двумерный массив 2x6

print(np.hsplit(a, 2))  # разбиение по горизонтали
print(np.vsplit(a, 2))  # разбиение по вертикали

print('---------')

a = np.arange(18)
a.resize(3, 3, 2)
print(a)
print(np.array_split(a, 2, axis=2))
print(np.array_split(a, 3, axis=0))
print(np.array_split(a, 3, axis=1))