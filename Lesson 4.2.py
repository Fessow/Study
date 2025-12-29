import re

text = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type " content="text/html; charset=windows-1251">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<p align=center>Hello World!</p>
</body>
</html>"""

match = re.findall(r"([-\w]+)[ \t]*=[ \t]*(?P<q>[\"'])?(?(q)([^\"']+(?<![ \t]))|([^ \t>]+))", text, re.MULTILINE)
print(match)

match = re.findall(r"""([-\w]+)             #выделяем атрибут
                   [ \t]*=[ \t]*            #далее, должно идти равно и кавычки
                   (?P<q>[\"'])?            #проверяем наличие кавычки
                   (?(q)([^\"']+(?<![ \t]))|([^ \t>]+))     #выделяем значение атрибута
                   """,
                   text, re.MULTILINE|re.VERBOSE)

print(match)

'''где flags – один или несколько флагов. Причем, их имена, следующие:

a – то же самое, что и re.ASCII;
i – соответствует re.IGNORECASE;
m – для re.MULTILINE;
s – для re.DOTALL;
x – для re.VERBOSE.'''


text = "Python, python, PYTHON"
match = re.findall(r"(?im)python", text)
print(match)
