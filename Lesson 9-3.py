
import numpy as np

b = np.array([1, 2, np.nan, np.inf, -np.inf])
print(b)

print(np.isinf(b))  # array([False, False, False,  True,  True])
print(np.isnan(b))  # array([False, False,  True, False, False]))

indx = np.isinf(b)
print(b[~indx])  # array([ 1.,  2., nan])

# для массива b = np.array([1, 2, np.nan, np.inf, -np.inf])
print(np.isfinite(b)) # array([ True,  True, False, False, False])

a = np.array([1+2j, 3-4j, 5])  # array([1.+2.j, 3.-4.j, 5.+0.j])
print(np.iscomplex(a)) # array([ True,  True, False])

print(np.isreal(a)) # array([False, False,  True]))

print(np.isreal(b))

