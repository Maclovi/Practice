# Данные, число пользователя
print('Привет!\nДобро пожаловать в калькулятор конвертирования\nразличных систем исчисления.')

# Массивы систем счисления
x_2=[0, 1]
x_4=[0, 1, 2, 3, 4]
x_8=[0, 1, 2, 3, 4, 5, 6, 7]
x_10=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x_16=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
x_16_str= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

# Калькулятор системы исчисления ковертирования в 10-тичную
def th_10(data, system):
    if system > 9:
        calculator = 0
        for i in range(len(data) - 1, -1, -1):
            if data[(len(data) - i - 1)].isalpha():
                calculator += x_16.index(data[(len(data) - i - 1)]) * system ** i
            else:
                calculator += x_16.index(int(data[len(data) - i - 1])) * system ** i
        return calculator
    return sum([int(data[len(data) - i - 1]) * system ** i for i in range(len(data) - 1, -1, -1)])

# Калькулятор конвертирования системы исчисления из 10-ой на другую
def th_all(data, system):
    calculator = []
    while int(data) != 0:
        calculator = [str(int(data) % system)] + calculator
        data = int(data) // system
    if system > 9:
        for i in range(len(calculator)):
            calculator[i] = x_16_str[int(calculator[i])]
        return ''.join(calculator)
    return int(''.join(calculator))

# Данные пользователя а также вызов функций
while True:
    toggle = input('Ты хочешь конвертировать в 10-ую или\nнаооброт с 10-ой на другую систему исчисления?\n(1 - конвертировать, 2 - другое)\n')
    while toggle.lower() != '1' and toggle.lower() != '2':
        toggle = input('Вы ввели недопустимое значение, повтори:\n')
    if toggle == '1':
        system = int(input('Какую систему исчисления хочешь перевести в 10-ую?\nВведи цифру(2-16):\n'))
        while not 2 <= system <= 16:
            system = int(input('Вы ввели недопустимое значение, повтори попытку:\n'))
        data = input('Введи цифры для конвертирования:\n')
        while len([i for i in data if i not in x_16_str]) > 0:
            data = input('Данное значение отсутствует в калькуляторе -\nПовторите попытку:\n')
        print('Ваше значение в', str(system) + '-ом', 'исчисление:', th_10(data, system))
        answer = input('Желаете продолжить?(да, нет)\n')
        while answer.lower() != 'да' and answer.lower() != 'нет':
            answer = input('Вы ввели недопустимое значение, повторите:\n')
        if answer.lower() == 'да':
            continue
        else:
            print('До новый встреч!')
            break
    elif toggle == '2':
        system = int(input('В какую систему исчисления перевести из 10-ой?\nВведи цифру(2-16):\n'))
        while not 2 <= system <= 16:
            system = int(input('Вы ввели недопустимое значение, повтори попытку:\n'))
        data = input('Введи цифры для конвертирования:\n')
        while len([i for i in data if i not in x_16_str]) > 0:
            data = input('Данное значение отсутствует в калькуляторе -\nПовтори попытку:\n')
        print('Ваше значение в', str(system) + '-ом', 'исчисление:', th_all(data, system))
        answer = input('Желаете продолжить?(да, нет)\n')
        while answer.lower() != 'да' and answer.lower() != 'нет':
            answer = input('Вы ввели недопустимое значение, повторите:\n')
        if answer.lower() == 'да':
            continue
        else:
            print('До новый встреч!')
            break
