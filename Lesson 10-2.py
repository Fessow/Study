import numpy as np

a = np.arange(10) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

np.random.shuffle(a) # array([8, 7, 9, 6, 3, 4, 0, 2, 1, 5])
np.random.shuffle(a) # array([7, 2, 1, 5, 8, 6, 4, 3, 9, 0])
print(a)
a = np.arange(1, 10).reshape(3, 3)
print(a)
np.random.shuffle(a)
print(a)
print('aaa')
print(np.random.permutation(10)) # array([8, 2, 7, 1, 0, 5, 3, 9, 4, 6])
