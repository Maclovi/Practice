import random
print('Добро пожаловать в числовую угадайку!')

right = int(input('Введите правую границу числа, счёт от 1-го:\n'))
num = random.randint(1, right)
def is_valid(integer):
    return 1 <= integer <= right

def game_randomint():  
    counter = 0
    while True:
        integer = int(input('Введите число, для отгадывания: '))
        if is_valid(integer) == False:
            print('А может быть все-таки введем целое число от 1 до ', right)
        elif integer > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            counter += 1
        elif integer < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            counter += 1
        else:
            print('Количество попыток:', counter)
            print('Вы угадали, поздравляем!')
            while True:
                continue_end = input('Продолжить игру? Напишите \'да\' или \'нет\'\n')
                if continue_end != 'нет' and continue_end != 'да':
                    print('Неверное значение, напишите ещё раз\n')
                elif continue_end == 'нет':
                    return ('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                elif continue_end == 'да':
                    counter = 0
                    break
                
print(game_randomint())
