import numpy as np

a = np.arange(1, 82).reshape(3, 3, 3, 3)
print(a)

print(a[1, 2, 0, 1]) # число 47
print(a[:, 1, :, :]) # матрица 3x3x3
print(a[0, 0])  # двумерная матрица 3x3
print(a[0, 0, :, :])
print(a[:, :, 1, 1]) # матрица 3x3
print(a[0:2, 0:2, 1, 1]) # матрица 2x2)
print(a[..., 1, 1]) # эквивалент a[:, :, 1, 1]