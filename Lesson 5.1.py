import re

text = "<font color=#CC0000 bg=#ffffff>"
match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(match)

print('то второй атрибут никак не будет фигурировать в результатах объекта match:')
print(match.groups())

#Если нужно найти все совпадения, то можно воспользоваться методом

for m in re.finditer(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text):
    print(m.groups())

#Однако, часто на практике нам нужно получить лишь список найденных вхождений, групп и это проще реализовать с помощью метода
#re.findall(pattern, string, flags)
match = re.findall(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(match)