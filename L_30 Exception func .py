def func2():
    try:
        return 1/0
    except:
        print('func 2 error') #Уже отловило тут, и далее не отлавливаает

def func1():
    try:
        return func2()
    except:
        print('func 1 error')


func1()