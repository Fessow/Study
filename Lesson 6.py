import numpy as np

a = np.array([(1, 2), (3, 4)])
b = np.array([(5, 6), (7, 8)])

x = np.hstack([a, b])  # объединение по оси axis1 (размерность 2x4)
y = np.vstack([a, b])  # объединение по оси axis0 (размерность 4x2)

z = np.vstack([b,a,a])
print(z)

a = np.fromiter(range(18), dtype='int32')
b = np.fromiter(range(18, 36), dtype='int32')
print(a)
print(b)
a.resize(3, 3, 2)
b.resize(3, 3, 2)
print(a)
print('!!!!!!!!!!')
print(b)
print('----------------')
c = np.hstack([a,b])
print(c)
print(c.shape)

print('----------------')
a = np.fromstring('1 2 3 4', sep = ' ')
b = np.fromstring('5 6 7 8', sep = ' ')
print(np.hstack([a, b]))
print(np.vstack([a, b]))
print(np.column_stack([a, b]))


a = np.arange(1, 13)
b = np.arange(13, 26)
a.resize(3, 3, 2)
b.resize(3, 3, 2)

c0 = np.concatenate([a, b], axis=0) # размерность 6x3x2
c1 = np.concatenate([a, b], axis=1) # размерность 3x6x2
c2 = np.concatenate([a, b], axis=2) # размерность 3x3x4