import re

text = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<script type="text/javascript">
let o = document.getElementById('id_div');
console.log(obj);
</script>
</body>
</html>"""

# NOT OK
match = re.findall(r"^<script.*?>([\w\W]+)(?=</script>)", text, re.MULTILINE)
print(match)
# NOT OK
match = re.findall(r"^<script.*?>(.+)(?=</script>)", text, re.MULTILINE)
print(match)
# OK
match = re.findall(r"^<script.*?>([\w\W]+)(?<=</script>)", text, re.MULTILINE)
print(match)

#атрибут=значение
# OK
match = re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"']([^\"']+)(?<![ \t])", text, re.MULTILINE)
print(match)

# NOT OK??
match = re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"'](.+?)(?<![ \t])[\"']", text, re.MULTILINE)
print(match)

