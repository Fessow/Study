import numpy as np
a = np.array([1, 2, 3, 10, 20, 30])

print(a[a>5])
print(a>5)

b = np.array([1, 2, 3, 4, 5, 6])

print(a == b)    # array([ True,  True,  True, False, False, False])
print(a >= b)    # array([ True,  True,  True,  True,  True,  True])
print(a <= b)    # array([ True,  True,  True, False, False, False])
print(a != b)    # array([False, False, False,  True,  True,  True])

print(a!=2)

print(np.greater(a, b)) # array([False, False,  True, False]) a>b
print(np.less(a, b)) # array([ True,  True, False, False]) a<b
print(np.equal(a, b)) # array([False, False, False,  True]) a==b

#if(a == b):
    #print("a == b") NOT WORK

if np.array_equal(a ,b):
     print("a == b")

print(np.any(a > 5))    # True
print(np.any(a == 5))    # False
print(np.any(a == b))    # True


print(np.all(a > 5))       # False
print(np.all(a > 0) )      # True
print(np.all(a == b))     # False