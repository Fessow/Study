import numpy as np

print(np.random.rand()) # вещественное случайное число от 0 до 1
print(np.random.rand(5)) # array([0.78191696, 0.66581136, 0.46458873, 0.76416839, 0.28206656]))
print(np.random.rand(2, 3)) # массив 2x3)
print(np.random.randint(10)) # генерация целых чисел в диапазоне [0; 10)
print(np.random.randint(5, 10)) # генерация в диапазоне [5; 10)

print(np.random.randint(5, size=4)) # array([3, 1, 1, 4])
print(np.random.randint(1, 10, size=(2, 5))) # матрица 2x5)

'''Функции rand() и randint() генерируют числа с равномерным законом распределения. 
Если нужно получать значения с другими широко известными распределениями, то используются функции:'''

print(np.random.randn()) # нормальная СВ с нулевым средним и единичной дисперсией
print(np.random.randn(5)) # массив из пяти нормальных СВ
print(np.random.randn(2, 3)) # матрица 2x3 из нормальных СВ
print(np.random.pareto(2.0, size=3)) # распределение Паретто с параметром 2,0
print(np.random.beta(0.1, 0.3, size=(3, 3))) # бета-распределение с параметрами 0,1 и 0,3)

print('aaaa')

np.random.seed(13) # начальное значение генератора случайных чисел)
print(np.random.randint(10, size=10)) # array([2, 0, 0, 6, 2, 4, 9, 3, 4, 2]))
print(np.random.randint(10, size=10)) # array([6, 5, 9, 4, 2, 0, 3, 5, 3, 6])
np.random.seed(13)
print(np.random.randint(10, size=10)) # array([2, 0, 0, 6, 2, 4, 9, 3, 4, 2])
print(np.random.randint(10, size=10)) # array([6, 5, 9, 4, 2, 0, 3, 5, 3, 6]))