e = ZeroDivisionError('Деление на ноль')
# Все исключения должны наследоваться от базового класса BaseException
#raise e
class ExceptionPrint(Exception): #Главный класс исключений
    '''Общий класс исключения принтера '''


class ExceptionPrintSendData(ExceptionPrint): # Дают возможность сделать свою иерархию исключений
    # Дочерний класс исключений
    '''Класс исключения при отправке данных принтеру '''
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'ОШИБКА:{self.message}'

class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f'Печать:{str(data)}')

    def send_data(self,data):
        if not self.send_to_print(data):
            #raise Exception('Принтер не отвечает') #Соотвественно генериурется исключение
    #ОСНОВЫВАЕМСЯ ВСЕГДА НА КЛАССЕ EXCEPTION
            raise ExceptionPrintSendData('Принтер не отвечает')
    def send_to_print(self, data):
        return False # В данном случае, не могут, т.к всегда False

p = PrintData()
try:
    p.print('123')
#except Exception:
except ExceptionPrintSendData:  # Специализированное исключение
    print('Принтер не отвечает')
except ExceptionPrint:
    print('Общая ошибка печати') # общее исключение

p.print('123')