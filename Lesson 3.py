import numpy as np

#empty(shape,...)
#eye(N,M=None)
#identity(n,...)
#ones(shape, ...)
#zeros(shape,...)
#full(shape,value)

'''print(np.array([0]*10))
print(np.empty(5, dtype='int16'))
print(np.empty((3,3), dtype='int16'))
print(np.eye(3))
print(np.eye(4,2))

print(np.identity(5))
print(np.zeros( (2,3,4)))
print(np.ones([4,3], dtype='int'))'''


"asmatrix(object, )" \
"diag(list, )" \
"diagflat(list, )" \
"tri(N,M=None, )" \
"tril(list, )" \
"triu(list, )" \
"vander(list, N=none, )"

'''print(np.asmatrix('1 2 3 4')) #матрица из строки
print(np.asmatrix('1 2; 3 4'))
print(np.asmatrix([4, 3, 2]))
print(np.diag([1,2,3]))'''


'''print(np.diag(([1,2,3],[4,5,6],[7,8,9])))
print(np.diagflat(([1,2,3],[4,5,6],[7,8,9])))
print(np.tri(4))
print(np.tri(4,2))
a = np.array( [(1,2,3),(4,5,6),(7,8,9)])
print(np.tril(a))
print(np.triu(a))
print(np.tril([1,2,3]))
print(np.vander([1,2,3]))'''

#arange()
#linspace(start, stop, )
#logspace(start, stop, )
#geomspace(start, stop, )
#meshgrid(x1,....,xn, ...)
#mgrid[]
#ogrid[]

'''print(np.arange(5))
print(np.arange(2,6,0.5))
print(np.cos(np.arange(0,np.pi,0.1)))
print(np.linspace(0, np.pi, 3))
print(np.logspace(0,1,4))
print(np.geomspace(1,16,5))'''

b = np.array([(1,2), (3,4)])
z = np.copy(b)

def getRange(x,y):
    return 100*x + y

c = np.fromfunction(getRange, (2,2))
print(c)

c = np.fromfunction(lambda x, y: x*100 + y, (2,2))
print(c)

print(np.fromiter('hello', dtype='U1'))

def my_generator(N):
    for i in range(N):
        yield i

d = np.fromiter(my_generator(4), dtype='int8')
print(d)

e = np.fromstring('1 2 3', dtype='int16', sep=' ')
print(e)

e = np.fromstring('1,2,3', dtype='int16', sep=',')
print(e)