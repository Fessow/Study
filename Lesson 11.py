import numpy as np

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(10, 19).reshape(3, 3)
print(a*b)

print(np.dot(a,b))
print(np.dot(b,a))

#Считается, что этот вариант предпочтительнее использовать при умножении матриц.
print(np.matmul(a, b))

