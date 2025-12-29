#getitem - получение значения по ключу item
#setitem - запись значения value по ключу key
#delitem - удаление элемента по ключу key

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)
    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('Неверный Индекс')

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:#если out of range
            raise TypeError('Индекс должен быть неотрицательным целым числом')

        if key >= len(self.marks):  #если out of range
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):#если out of range
            raise TypeError('Индекс должен быть неотрицательным целым числом')

        del self.marks[key]


s1 = Student('sergey', [5,5,3,4,5])

print(s1[2])

s1[2] = 4
print(s1.marks)

s1[10] =4
print(s1.marks)

del s1[2]
print(s1.marks)