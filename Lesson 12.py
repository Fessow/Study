import numpy as np

a = np.array([1, 2, 3, 4, 4, 3, 2, 1])

setA = np.unique(a) # array([1, 2, 3, 4])
print(setA)

print(np.unique(a, return_counts=True)) # (array([1, 2, 3, 4]), array([2, 2, 2, 2]))
print(np.unique(a, return_index=True)) # (array([1, 2, 3, 4]), array([0, 1, 2, 3])))
print(np.unique(a, return_inverse=True)) #возвращает индексы, по которым можно точно восстановить исходный массив

setA, indx = np.unique(a, return_inverse=True)
aa = setA[indx] # array([1, 2, 3, 4, 4, 3, 2, 1])
print(aa) #восстановление исходного массива a
print('aaaaa')
x = np.array([[0, 1, 1, 2],[0, 1, 1, 2],[9, 1, 1, 2]])
print(np.unique(x)) # array([0, 1, 2, 9])
print(np.unique(x, axis=0)) #определялись уникальные строки
print(np.unique(x, axis=1)) #получим уникальные столбцы: