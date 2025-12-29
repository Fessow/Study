import re

phone = "89123456789"
match = re.findall(r"8\d{10}", phone)

print(match)

text = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
match = re.findall(r"\w+\s*=\s*[^;]+", text)
print(match)
match = re.findall(r"(\w+)\s*=\s*([^;]+)", text)
print(match)

text = "Картинка <img src='bg.jpg'> в тексте</p>"
match = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]*>", text)

text1="<p>Картинка <img alt='картинка' src='bg.jpg'> в тексте</p>"
text2="<p>Картинка <img src='bg.jpg'> в тексте</p>"
text3="<p>Картинка <img src='bg.jpg' title='картинка'> в тексте</p>"

def ifpic(text):
    return re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]*>", text)

pics = [text1, text2, text3]
res = (list(map(ifpic, pics)))
print(res)

print(*list(map(lambda x: re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]*>", x), pics)))