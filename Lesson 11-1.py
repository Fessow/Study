import numpy as np

a = np.arange(1, 10)
b = np.ones(9)
print(np.dot(a, b)) # значение 45

print(np.inner(a,b))
print(np.outer(a,b))

print( a @ b)
a.resize(3,3)
b.resize(3,3)
print(a @ b)