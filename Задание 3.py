documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}







# все ,что касается KeyError:






def KeyErrors(answer):
    p = 0

    for temp in documents:
        try:
            temp[answer]
        except KeyError:
            print('ошибка: Key Error сработал')
        else:
            print(f'данный ключ еть у документа под номером {p+1} есть, программа работает отлично')
        p+=1





# вызывается на каждой итереации цикла







def conclusion(answer):
    if answer == 'yes':

        print('вывод списка документов ', documents, sep='\n')
        print('полки ', directories)
    else:
        print('значение не будет выведено на экран\n')
    return None


def reminder(answer):
    if answer == 'yes':
        print('Памятка по работе с функциями', 'для выполнения функции p_people напечатайте people',
              'для выполнения функции s_shelf напечатайте shelf', 'для выполнения функции l_list напечатайте list',
              'для выполнения функции a_add напечатайте add', 'для выполнения функции d_delete напечатайте delete ',
              'для выполнения функции m_move напечатайте move ', 'для выполнения функции as_add_shelf напечатайте as ',
              'для выхода напечатайте quit', sep='\n')
    else:
        print('продолжается работа без памятки\n')

    return None


def choose_func(call_comand):
    if call_comand == 'people':

        print('работа функции p_people:')

        number = input('введите номер документа:')

        p_people(number)

    elif call_comand == 'shelf':

        print('работа функции s_shelf:')

        num = input('введите номер документа:')

        s_shelf(num)
    elif call_comand == 'list':

        print('работа функции l_list:')

        l_list()

    elif call_comand == 'add':
        print('работа функции a_add')

        print('введите данные :\n')

        tip = input('введите тип документа:')

        number = input('введите число:')

        name = input('введите имя:')

        polka = input('введите номер полки:')

        a_add(tip, number, name, polka)

    elif call_comand == 'move':
        print('работа функции m_move:')
        number = input('введите номер документа:')
        number_polka = input('введите номер полки:')
        m_move(number, number_polka)

    elif call_comand == 'delete':
        print('работа функции d_delete:')
        number = input('введите номер документа:')
        d_delete(number)

    elif call_comand == 'as':
        print('работа функции as_add_shelf:')
        number = input('введите номер новой полки:')
        as_add_shelf(number)

    elif call_comand == 'quit':
        print('вы завершили работу с функциями')

    else:
        print('\nданная функция не опознана')

    return None


def as_add_shelf(number_new_polka):
    if number_new_polka not in directories.keys():
        directories[number_new_polka] = []
        print(f'полка под номером {number_new_polka} успешно добавлена')
    else:
        print('такая полка уже существует')

    return None


def m_move(number_documentation, number_polka):
    proverka_na_nalichie_doc = 0
    perenos = ''

    proverka_na_polky = 0

    for keys, values in directories.items():
        if keys == number_polka:
            proverka_na_polky += 1
            break

    for values in directories.values():
        for numbers in values:
            if numbers == number_documentation:
                proverka_na_nalichie_doc += 1

    if proverka_na_polky == 0:
        print('возникла ошибка:такой полки нет')
        return None

    elif proverka_na_nalichie_doc == 0:
        print('возникла ошибка:такого документа нет')
        return None

    elif proverka_na_nalichie_doc and proverka_na_polky == True:

        for keys, values in directories.items():
            p = 0
            for numbers in values:
                if numbers == number_documentation:
                    perenos = number_documentation
                    del (values[p])
                    print('документ был найден')

                p += 1

        p = 0
        for keys, values in directories.items():
            if keys == number_polka:
                values.append(perenos)
                print(f'объект был перемещен на полку {number_polka}')
                return None
            p += 1


def d_delete(number_documentation):
    proverka_na_nalichie_doc = 0

    for lists in documents:
        p = 0
        for keys, values in lists.items():
            if number_documentation == values:
                proverka_na_nalichie_doc = 1
            p += 1

    if proverka_na_nalichie_doc == 0:
        print('документ не найден и значение не удалилось\n')
        return None

    for values in directories.values():
        p = 0
        for numbers in values:
            if numbers == number_documentation:
                del (values[p])
                print(f'значение {number_documentation} было удалено')
                return None
            p += 1

    return None


def p_people(number_documentation):
    perem = 0
    for temp in documents:

        for tip, value in temp.items():

            if value == number_documentation:
                perem += 1
                print('найденное значение:')
                print(temp['name'])
                break

    if perem != 1:
        print('такого значения не найдено/n')

    return None


def s_shelf(number_documentation):
    perem = 0
    for keys, values in directories.items():
        for val in values:
            if val == number_documentation:
                perem += 1
                print(f'ваше значение находится на полке {keys}')
                break

    if perem != 1:
        print('такого значения нет\n')
    return None


def l_list():
    for temp in documents:

        for tip, value in temp.items():
            print(value, end=' ')
        print('\n\n')

    return None


def a_add(doc_type, doc_val, doc_name, directories_number):
    new_doc = {}
    new_doc['type'] = doc_type
    new_doc['number'] = doc_val
    new_doc['name'] = doc_name

    perem = 0
    for key, massive in directories.items():  # добавление в directories
        if key == directories_number:
            perem = 1
            documents.append(new_doc)  # добавление в documents
            massive.append(doc_val)
            break

    if perem == 1:
        print(f'значение было добавлено на полку {directories_number}')
    else:
        print('такой полки не оказалось и значение не добавилось\n')

    return None


call_comand = ' '
# выполнение программы
while call_comand != 'quit':
    answer = input('вы хотите вывести памятку на экран  :')

    reminder(answer)

    call_comand = input('\nвведите название функции,которую хотите вызвать:')

    choose_func(call_comand)

    answer = input('вы хотите вывести текущий список и полки на экран  :')
    conclusion(answer)





# само расширение
    answer = input('введите ключ ,который хотите проверить:')
    KeyErrors(answer)

