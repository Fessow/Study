import numpy as np
X = np.array([True, False, True, False])
Y = np.array([True, True, False, False])

print(np.logical_and(X, Y)) # логическое И: array([ True, False, False, False])
print(np.logical_or(X, Y)) # логическое ИЛИ: array([False,  True, False,  True])
print(np.logical_not(X)) # логическое НЕ: array([False,  True, False,  True])
print(np.logical_xor(X, Y)) # XOR: array([False  True  True False]))


a = np.array([1, 0, 2, 0])
b = np.array([3, 4, 0, 0])
print(np.logical_and(a, b)) # array([ True, False, False, False]))



