import random
# Строковые константы
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
exclude = 'il1Lo0O'
chars_user = ''

# Функция генерации пароля
def generation_password(lenght, chars):
    if len(chars) >= int(lenght):
        return ''.join(random.sample(chars, int(lenght)))
    else:
        for i in range(int(lenght) - len(chars)):
            chars += chars[i]
        return ''.join(random.sample(chars, int(lenght)))


# Вопросы пользователю, считывание данных
while True:
    numbers_passwords = input('Количество паролей? Введи цифру: ')
    if numbers_passwords.isdigit():
        break
    else:
        print('Введены неверные данные, попробуй ещё раз')
        continue

while True:
    password_length = input('Длина одного пароля? Введи цифру: ')
    if password_length.isdigit():
        break
    else:
        print('Введены неверные данные, попробуй ещё раз')
        continue

while True:
    add_numbers = input('Включать ли цифры: 0123456789 ?\nНапишите \'да\' или \'нет\'\n')
    if add_numbers != 'да' and add_numbers != 'нет':
        print('Может всё таки напишите, то что требуется от вас?')
        continue
    elif add_numbers == 'да':
        chars_user += digits
        break        
    else:
        break

while True:
    add_lowercase = input('Включать ли прописные символы: abcdefghijklmnopqrstuvwxyz ?\nНапишите \'да\' или \'нет\'\n')
    if add_lowercase != 'да' and add_lowercase != 'нет':
        print('Может всё таки напишите, то что требуется от вас?')
        continue
    elif add_lowercase == 'да':
        chars_user += lowercase_letters
        break        
    else:
        break

while True:
    add_uppercase = input('Включать ли строчные символы: ABCDEFGHIJKLMNOPQRSTUVWXYZ ?\nНапишите \'да\' или \'нет\'\n')
    if add_uppercase != 'да' and add_uppercase != 'нет':
        print('Может всё таки напишите, то что требуется от вас?')
        continue
    elif add_uppercase == 'да':
        chars_user += uppercase_letters
        break        
    else:
        break

while True:
    add_chars = input('Включать ли символы: !#$%&*+-=?@^_. ?\nНапишите \'да\' или \'нет\'\n')
    if add_chars != 'да' and add_chars != 'нет':
        print('Может всё таки напишите, то что требуется от вас?')
        continue
    elif add_chars == 'да':
        chars_user += punctuation
        break        
    else:
        break

while True:
    exclude_chars = input('Исключать ли неоднозначные символы:  il1Lo0O ?\nНапишите \'да\' или \'нет\'\n')
    if exclude_chars != 'да' and exclude_chars != 'нет':
        print('Может всё таки напишите, то что требуется от вас?')
        continue
    elif exclude_chars == 'да':
        chars_user = list(chars_user)
        for i in exclude:
            if i in chars_user:
                chars_user.remove(i)
        chars_user = ''.join(chars_user)
        break
    else:
        break
    
# Вызов функции в цикле
for i in range(int(numbers_passwords)):
    print(generation_password(password_length, chars_user))
