import numpy as np

a = np.arange(1, 10).reshape(3,3)
b = np.array([4, 5, 6])


print(a+b) # array([[ 5,  7,  9],   [ 8, 10, 12],   [11, 13, 15]]))

# a: 3 x 3
# b: 1 x 3

a = np.arange(6).reshape(3, 1, 2)
b = np.ones(4).reshape(2, 2)
print('!!!!!!!!!!!!!!!!!!!!!')
print(a)
print(b)

c=a*b
print(c.shape)# массив размерностью (3, 2, 2))
# a:  3  x 1 x 2
# b: (1) x 2 x 2


# a:  3  x (2) x 2
# b: (3) x  2  x 2

a=a.reshape(2,3,1)
#c=a*b # error

b=np.ones(6).reshape(3,2)
c = a*b
print(c.shape)
print(c)