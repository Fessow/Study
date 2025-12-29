import re

text = "(еда), еда, победа"
match = re.findall(r".", text)
print(match)

match = re.findall(r"\w", text, re.ASCII)
print(match)

text = "Еда, беду, из-за, победа"
match = re.findall(r"[-0-9]", text)
print(match)

match = re.findall(r"[а-я]", text)
print(match)

text = "(еда), еда, победа"
match = re.findall(r"[(]еда[)]", text)

text = "Еда, беду, победа"
match = re.findall(r"[еЕ]д[ау]", text)
print(match)


text = "Еда, беду, 5 победа"
match = re.findall(r"[0-9]", text)
print(match)

match = re.findall(r"[^0-9]", text)
print(match)

