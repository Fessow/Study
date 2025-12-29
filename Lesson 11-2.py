import numpy as np

a = np.array([1,2,3])
b = np.arange(4,10).reshape(3,2) # матрица 3x2

print(np.dot(a,b))
#print(np.dot(b,a))

a = np.array([1, 2])
print(np.dot(b, a)) # array([14, 20, 26])

a.shape = -1, 1 # вектор-столбец 2x1
print(np.dot(b, a)) # вектор-столбец 3x1)
