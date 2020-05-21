def operation(symbols):
    if symbols[0] == '+':
        try:
            float(symbols[1]) + float(symbols[2])
        except ValueError:
            return 'ошибка :не все аргументы - числа'
        else:
            if float(symbols[1]) > 0 and float(symbols[2]) > 0:
                return float(symbols[1]) + float(symbols[2])
            return 'ошибка:не все аргументы - положительные числа'

    elif symbols[0] == '-':

        try:
            float(symbols[1]) - float(symbols[2])
        except ValueError:
            return 'ошибка :не все аргументы - числа'
        else:
            if float(symbols[1]) > 0 and float(symbols[2]) > 0:
                return float(symbols[1]) - float(symbols[2])
            return 'ошибка:не все аргументы - положительные числа'

    elif symbols[0] == '*':
        try:
            float(symbols[1]) * float(symbols[2])
        except ValueError:
            return 'ошибка :не все аргументы - числа'
        else:
            if float(symbols[1]) > 0 and float(symbols[2]) > 0:
                return float(symbols[1]) * float(symbols[2])
            return 'ошибка:не все аргументы - положительные числа'


    elif symbols[0] == '/':
        try:
            float(symbols[1]) / float(symbols[2])
        except ValueError:
            return 'ошибка :не все аргументы - числа'
        except ZeroDivisionError:
            return 'Ошибка:деление на ноль'
        else:
            if float(symbols[1]) > 0 and float(symbols[2]) > 0:
                return float(symbols[1]) / float(symbols[2])
            return 'ошибка:не все аргументы - положительные числа'


print('введите строку типа: + 12 0')

sym = ['+', '-', '*', '/']

s = input('ваша строка:').split()

A = list(s)

assert A[0] in sym, f'не опознанный арифметический оператор,мы работаем только с {sym}'

assert len(A) == 3, 'количество введенных элементов не совпадает с количеством доступных, так как доступно всего 3'


print(operation(A))