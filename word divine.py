import random
word_list = [
    'Александр', 'Альбина', 'Серёжа', 'Инга', 'Калузанова', 'Тимофей', 'Альбинос', 
    'Машина', 'Корабль', 'Рюкзак'
]
# Генерация рандомного слова
def get_word():
    return random.choice(word_list).upper()

# функция получения текущего состояния
def display_hangman(tires):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |     ⎛ ⎞
                   |
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |     ⎛
                   |
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |
                   |
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼
                   |
                   |
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      ▼
                   |
                   |
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                '''
    ]
    return stages[tires]

# Начало игры, основная логика игры
def play(word):
    word_completion = list('_' * len(word))  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []    # список уже названных букв
    guessed_letters = [word[i] for i in range(len(word)) if not 1 <= i < len(word) - 1]
    guessed_words = []                 # список уже названных слов
    tires = 6
    print('Давай играть в угадай слов!')   # Вступление
    while True:
        word_completion[0] = word[0]
        word_completion[-1] = word[-1]
        if tires == 0:  # На случай если потрачены попытки
            print('Ваше не отгаданное слово:', word)
            txt_handler = input('Увы, но вам не удалось отгадать слово.\nПродолжить игру?(1 - да, 2 - нет)\n')
            while txt_handler != '1' and txt_handler != '2':   # Защита
                txt_handler = input('Вы ввели неверный ответ.nПовторите:\n')
            if txt_handler == '1':
                tires = 6
                guessed_letters = []
                guessed_words += [word]
                word = get_word()
                word_completion = list('_' * len(word))
                guessed_letters = [word[i] for i in range(len(word)) if not 1 <= i < len(word) - 1]
                continue
            else:    # Выводит отгаданные слова  завершает игру
                guessed_words += [word]
                print('Ваши отгаданные слова:', '-'.join(guessed_words))
                return 'До новых встреч!'
        if word.title() in word_list[:7]:
            print('\nПодсказка: это ЧЕЛОВЕК')
        else:
            print('\nПодсказка: это НЕ ЧЕЛОВЕК')
        print('\nТекущее состояние игры:', display_hangman(tires), 'Начальные допустимые промахи:', tires)
        print('\nНачальное слово:', ''.join(word_completion))
        txt_handler = input('Введите букву или слово целиком:\n').upper()    # Слова игрока
        if txt_handler == word:
            print('\nНачальное слово:', word)
            txt_handler = input('\nПоздравлямба, вы угадали!!!\nПродолжить игру?(1 - да, 2 - нет)\n')
            while txt_handler != '1' and txt_handler != '2':   # Защита
                txt_handler = input('Вы ввели неверный ответ.nПовторите:\n')
            if txt_handler == '1':
                tires = 6
                guessed_letters = []
                guessed_words += [word]
                word = get_word()
                word_completion = list('_' * len(word))
                guessed_letters = [word[i] for i in range(len(word)) if not 1 <= i < len(word) - 1]
                continue
            else:    # Выводит отгаданные слова  завершает игру
                guessed_words += [word]
                print('Ваши отгаданные слова:', '-'.join(guessed_words))
                return 'До новых встреч!'
        while not txt_handler.isalpha() or (''.join(word_completion).count('_') != len(txt_handler) and len(txt_handler) != 1) or [i for i in txt_handler if i in guessed_letters]:  # Защита
            txt_handler = input('ОШИБКА!!!\n1.Вы ввели не алфавитные буквы/слово.\n2.Допустимо вводить 1 букву или целиком слово -\nили оставшиеся буквы.\n3.Данные слова повторять нельзя.\nЗапишите снова:\n').upper()
            if txt_handler == word:
                print('\nНачальное слово:', word)
                txt_handler = input('\nПоздравлямба, вы угадали!!!\nПродолжить игру?(1 - да, 2 - нет)\n')
                while txt_handler != '1' and txt_handler != '2':   # Защита
                    txt_handler = input('Вы ввели неверный ответ.nПовторите:\n')
                if txt_handler == '1':
                    tires = 6
                    guessed_letters = []
                    guessed_words += [word]
                    word = get_word()
                    word_completion = list('_' * len(word))
                    guessed_letters = [word[i] for i in range(len(word)) if not 1 <= i < len(word) - 1]
                    continue
                else:    # Выводит отгаданные слова  завершает игру
                    guessed_words += [word]
                    print('Ваши отгаданные слова:', '-'.join(guessed_words))
                    return 'До новых встреч!'            
        if txt_handler in word:   # Проверяет входят ли буквы/слова в состав слова
            guessed_letters += ''.join([i * word.count(i) for i in txt_handler])   # Добавляет в список названных букв
            guessed_letters = [i for i in guessed_letters]  # Дробин на списки, если букв в слове много
            for i in txt_handler:  # Заменяет символ в списке на угаданную букву игрока
                word_completion[word.find(i)] = i
                if word.count(i) > 1:
                    word_completion[word.rfind(i)] = i
                if word.count(i) == 3:
                    word_completion[word[word.find(i) + 1:].find(i) + word.find(i) + 1] = i  # Находит индекс
            if len(guessed_letters) == len(word):
                print('\nНачальное слово:', ''.join(word_completion))
                txt_handler = input('\nПоздравлямба, вы угадали!!!\nПродолжить игру?(1 - да, 2 - нет)\n')
                while txt_handler != '1' and txt_handler != '2':   # Защита
                    txt_handler = input('Вы ввели неверный ответ.nПовторите:\n')
                if txt_handler == '1':
                    tires = 6
                    guessed_letters = []
                    guessed_words += [word]
                    word = get_word()
                    word_completion = list('_' * len(word))
                    guessed_letters = [word[i] for i in range(len(word)) if not 1 <= i < len(word) - 1]
                    continue
                else:    # Выводит отгаданные слова  завершает игру
                    guessed_words += [word]
                    print('Ваши отгаданные слова:', '-'.join(guessed_words))
                    return 'До новых встреч!'
            else:
                tires -= 1
                print('\nУгадали частично, так держать!')
        else:
            tires -= 1
            print('Не, не угадали, давай по новой Уася!')


print(play(get_word()))
