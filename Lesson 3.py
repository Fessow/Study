import re

text = 'pi=3, a = 5'
text = 'lat =5, lon=7 ,a =5'



match = re.findall(r"(?:lat|lon)\s*=\s*\d+", text)

print(match)

match = re.findall(r"(lat|lon)\s*=\s*(\d+)", text)

print(match)


text = "Картинка <img src='bg.jpg'> в тексте</p>"
#match = re.findall(r"<img\s+[^>]*src=[\"'](.+?)[\"']", text)

match = re.findall(r"<img\s+[^>]*src=(?P<q>[\"'])(.+?)(?P=q)", text)

print(match)