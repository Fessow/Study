#Исключения в процессе компиляции - синтаксические ошибки. Это когда не запускается программа изначально
#Исключения в момент выполнения

try:
    f = open('myfile.txt')
except FileNotFoundError:
    print('Невозможно открыть файл') #программа аварийно не завершилась

print('Штатное завершение 1 ')

try:
    x,y = map(int, input().split())
    result = x/y
except (ValueError, ZeroDivisionError): #Можно писать сразу два, но так не рекомендуется
    print('Неверный тип данных') #программа аварийно не завершилась
#except ZeroDivisionError:
    #print('Деление на ноль')

# Блоков Эксепт может быть сколько угодно. В зависимости какая ошибка возможна такую и следуют прописывать
print('Штатное завершение 2')

try:
    x,y = map(int, input().split())
    result = x/y
except (ArithmeticError): # Класс арифметик ерор позволяет отслеживать все дочерние классы исклюений
    # это ZeroDevisionError
    # Floatin Point Error
    # Overflow Error
    print('Деление на ноль')

# Если написать класс Exception класс то он все будет отлавливать

try:
    x,y = map(int, input().split())
    result = x/y
except ValueError:
    print('Неверный тип данных')
except Exception:
    print('Деление на ноль')

# ЕСТЬ НЮАНС  ЕСЛИ МЫ ПОМЕНЯЕМ МЕСТАМИ VALUEERROR  Exception, то обработка Value вообще не будет происходить, потому что первый блок Exception отлавливает все исключения
# и до ValueError мы не дойдем

#поэтому сначала прописывается блок со специализированными исключениями, а потом с базовыми


#можно вообще прописать
try:
    x,y = map(int, input().split())
    result = x/y
except: # отлавливает вообще все
    print("Ошибка")
