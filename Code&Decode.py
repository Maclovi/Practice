
# Текстовые константы, генерация через однострочные выражения
alpha = [chr(i) for i in range(ord('а'), ord('я') + 1)] * 2
alpha += [chr(i) for i in range(ord('a'), ord('z') + 1)] * 2
alpha += [chr(i) for i in range(ord('А'), ord('Я') + 1)] * 2
alpha += [chr(i) for i in range(ord('A'), ord('Z') + 1)] * 2
alpha = ''.join(alpha)

# Декодирование текст, по кол-во символов в слове
def decodetxt(key, txt):
    decodetxt = ''
    for i3 in txt:
        if i3 in alpha:
            decodetxt += alpha[alpha.rfind(i3) - key]
        else:
            decodetxt += i3
    return decodetxt

# Кодирование текста, по кол-во символов в слове
def codetxt(key, txt):
    codetxt = ''
    for i3 in txt:
        if i3 in alpha:
            codetxt += alpha[alpha.find(i3) + key]
        else:
            codetxt += i3
    return codetxt


# Начало программы, приветствие
name = input('Привет! Добро пожаловать в шифровальную машину.\nКак тебя зовут?\n')
print(name + ',', 'Приятно познакомиться!')

# Запуск программы
while True:
    
    # Данные пользователя
    txt = input('Введи текст для дальнейших махинаций:\n',)
    txt1 = txt.split()  # Преобразует оригинальный текст в список со всеми символами
    txt2 = ''.join([q for i in txt for q in i if q.isalpha() or q.isspace()]).split()  # Удаляет все символы которые не входят в алфавит и преобразует в список

    # Ответ пользователя
    answer = input('Желаешь зашифровать сообщение или дешифровать?\n(з - зашифровать, д - дешифровать)\n')
    while answer.lower() != 'з' and answer.lower() != 'д':
        answer = input('Ты ввёл неверные данные, повтори ещё раз\n')
    if answer.lower() == 'з':
        for i in range(len(txt2)):
            key = len(txt2[i])
            print(codetxt(key, txt1[i]), end=' ')
    elif answer.lower() == 'д':
        for i in range(len(txt2)):
            key = len(txt2[i])
            print(decodetxt(key, txt1[i]), end=' ')
    print()
    answer1 = input('Желаешь продолжить?(да, нет)\n')
    while answer1.lower() != 'да' and answer1.lower() != 'нет':
        answer1 = input('Вы ввели неверные данные, повторите ещё раз\n')
    if answer1.lower() == 'нет':
        print('До новых встреч!')
        break
    else:
        continue
