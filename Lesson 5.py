import re

text = "<font color=#CC0000>"
match = re.search(r"#[\da-fA-F]{6}\b", text)
print(match)

match = re.search(r"#[\da-fA-F]{7}\b", text)
print(match)


match = re.search(r"(\w+)=(#[\da-fA-F]{6})\b", text)
print(match)

print(match.group(0))
print(match.group(1))
print(match.group(2))

print('На выходе получим кортеж из соответствующих вхождений:')
print(match.group(0,1,2))

print('Возвращает кортеж из всех групп, начиная с индекса 1. У этого метода есть необязательный параметр default, который определяет возвращаемое значение для групп, не участвующих в совпадени')
print(match.groups())

print('Свойство lastindex содержит индекс последней группы')
print(match.lastindex)

print('Если нам нужно узнать позиции в тексте начала и конца группы, то для этого служат методы start и end')
print(match.start(1))
print(match.end(1))

print('Если по каким-то причинам группа не участвовала в совпадении (например, ее вхождение было от 0), ',
      'то данные методы возвращают -1.'
      ' Также мы можем получить сразу кортеж с начальной и конечной позициями для каждой группы:', sep='\n')
print(match.span(0))
print(match.span(1))

print('Для определения первого и последнего индексов, в пределах которых осуществлялась проверка в тексте, служат свойства:')
print(match.endpos)
print(match.pos)


pattern = match.re
print('возвращает скомпилированное регулярное выражение')
print(pattern)


print('содержит анализируемую строку.')
print(match.string)

match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print('Здесь определили две именованных группы: key и value.')
print(match)

print(match.groupdict())

print('возвращает имя последней группы (или значение None, если именованных групп нет)')
print(match.lastgroup)

print('формировать строку с использованием сохраненных групп')
print(match.expand(r"\g<key>:\g<value>"))

