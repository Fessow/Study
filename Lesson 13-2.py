import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5])
c = np.array([7, 8, 9, 10])
print(a)
print(b)
print(c)
#print(a * b + c) # ошибка, размеры не согласованы

# a: 1 x 1 x 3
# b: 1 x 2 x 1
# c: 4 x 1 x 1

a.shape = 1, 1, -1
b.shape = 1, -1, 1
c.shape = -1, 1, 1

x = [[[1, 2, 3]]]
y= [[[4], [5]]]
z=[[[ 7]], [[ 8]], [[ 9]], [[10]]]

res = a*b + c
print(res.shape)

a = np.array([1, 2, 3])
b = np.array([4, 5])
c = np.array([7, 8, 9, 10])
an, bn, cn = np.ix_(a, b, c)

print(an.shape)
print(bn.shape)
print(cn.shape)

print(an * bn + cn) # массив 3x2x4

