def get_values():
    try:
        x, y = map(int, input().split())
        return x, y
    #Переменная Z является ссылкой на экземпляр класса исключения и мы можем исп ее для вывода исключения в консоль
    except ValueError as z:
        print(z)
        return 0, 0
    #except ZeroDivisionError as z:
        #print(z)
#можно дополнительно прописать блок else при штатном выполнении блока трай, если не произошло никаких ошибок
#else:
    #print('Исключений не произошло')
    finally: # Этот блок выполняется всегда независимо от того произошли какие-то исключения или не произошли
        print('БЛОК finally выполнился ')
    # СНАЧАЛА ВЫПОЛНИЛСЯ БЛОК FINALLY если данные корректны
    # СНАЧАЛА ВЫПОЛНИЛСЯ БЛОК FINALLY если данные некорректны
    # !!!!!!!!!И ПОТОМ В САМОМ КОНЦЕ ОТРАБОТАЛ RETURN!!!!!!1

x, y = get_values()
print(x, y)



#Вложенные блоки
try:
    x, y = map(int, input().split())
    try:
        res = x/y
    except ZeroDivisionError:
        print('Деление на ноль')
except ValueError as z:
    print(z)


def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return ('Деление на ноль')
res = 0
try:
    x, y = map(int, input().split())
    res = div(x,y)
except ValueError as z:
    print(z)

print(res)




try:
    with open('myfile.txt') as f:
        f.write('hello')
except FileNotFoundError as z:
    print(z)
except:
    print('Другая ошибка')




