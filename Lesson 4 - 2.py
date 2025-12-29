import numpy as np


#добавление осей
#np.expand_dims(a, axis) - добавление оси
#np.square(a[, axis]) - удаление оси

x_test = np.arange(32).reshape(8, 2, 2)
print(x_test)

print(x_test.shape)

x_test4 = np.expand_dims(x_test, axis =0)
print(x_test4.shape)

x_test4[0,0,0,0] = -100

print(x_test)

#опять же создает лишь представление массива добавляя новую ось, данные те же. копирование не происходит

a= np.append(x_test4, x_test4, axis = 0)
print(a.shape)

b = np.delete(a, 0, axis=0)
print(b.shape)

b = np.expand_dims(x_test4, axis=-1) #последняя ось
print(b.shape)

c = np.squeeze(b)
print(c.shape)

c = np.squeeze(b, axis = 0)
print(c.shape)

#c = np.squeeze(b, axis = 1)

a = np.arange(1,10)
b= a[np.newaxis, :]
print(b)
print(b.shape)

b= a[:, np.newaxis]
print(b)
print(b.shape)

c = a[np.newaxis, :, np.newaxis]
print(c.shape)
print(c)