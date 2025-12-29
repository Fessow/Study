import numpy as np
a = np.array([(1, 2, 3), (1, 4, 9), (1, 8, 27)])
print(np.linalg.matrix_rank(a)) # рангравен 3


y = np.array([10, 20, 30])
print(np.linalg.solve(a, y)) # array([-5.  , 10.   , -1.66666667]))

invA = np.linalg.inv(a) # вычисление обратной матрицы
print(invA)
print(invA @ y) # вычисление корней