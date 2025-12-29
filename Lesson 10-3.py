import numpy as np

x = np.array([1, 4, 3, 7, 10, 8, 14, 21, 20, 23])
y = np.array([4, 1, 6, 9, 13, 11, 16, 19, 15, 22])

print(np.median(x)) # 9.0

print(np.var(x)) # дисперсия СВX на основе реализации x
print(np.std(y)) # СКО СВY на основе реализации y

XY = np.vstack([x, y]) # матрица 2x10
print(XY)

print(np.corrcoef(XY))
print(np.cov(XY)) # ковариационная матрица размерностью 2x2)

print(np.correlate(x, y)) # array([1736]))