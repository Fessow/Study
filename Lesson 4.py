import re

text = "подоходный налог, доход"
match = re.findall(r"прибыль|обретение|\bдоход\b", text)

print(match)

match = re.findall(r"\b(?:прибыль|обретение|доход)\b", text)
print(match)