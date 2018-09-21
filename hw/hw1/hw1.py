import random

def get_a_word():
    while True:
        a = input('\nВыбирите категорию и введите только её номер:\n1 астрономия\n2 лингвистика\n3 искусство\n')
        if a == '1' or a == '2' or a == '3':
            with open(a + '.txt', 'r', encoding='utf-8') as f:
                slovo = random.choice(f.readline().split())
            break
        else:
            print('Такого варианта нет в списке, попробуйте ещё раз')           
    return slovo

def igra(slovo):
    attempts = 10
    guessed_letters = []
    tried_letters = ''
    my_dict = {
        10: 'У вас есть 10 попыток',
        9: ' |\n |\n |\n |\n |\n | осталось 9 попытoк',
        8: ' _____\n |\n |\n |\n |\n |\n | осталось 8 попытoк',
        7: ' _____\n |/ \n |\n |\n |\n |\n | осталось 7 попытoк',
        6: ' _____\n |/  |\n |\n |\n |\n |\n | осталось 6 попытoк',
        5: ' _____\n |/  |\n |   o\n |\n |\n |\n | осталось 5 попытoк',
        4: ' _____\n |/  |\n |   o\n |  / \n |\n |\n | осталось 4 попытки',
        3: ' _____\n |/  |\n |   o\n |  /| \n |\n |\n | осталось 3 попытки',
        2: ' _____\n |/  |\n |   o\n |  /|\ \n |\n |\n | осталось 2 попытки',
        1: ' _____\n |/  |\n |   o\n |  /|\ \n |  /  \n |\n | осталась 1 попытка'
    }
    while attempts:
        print(my_dict.get(attempts))
        quiz = ''
        for letter in slovo:
            if letter in guessed_letters:
                quiz += letter
            else:
                quiz += '_'
        print('Слово:', quiz)
        guessed_part = quiz.replace('_', '')
        if guessed_part == slovo:
            break
        while True:
            popytka = input('\nПопробуйте угадать какая буква есть в загаданном слове: ').lower()
            if popytka in tried_letters:
                print('Эта буква уже проверена')
            elif len(popytka) == 1 and popytka in 'ёйцукенгшщзхъфывапролджэячсмитьбю'and popytka not in tried_letters:
                tried_letters += popytka + ' '
                break
            else:
                print('Что-то не так, возможно это не буква кириллицы, попробуйте снова.')
        if popytka in slovo:
            guessed_letters.append(popytka)
            print('Эта буква есть в слове\nПроверенные буквы:', tried_letters)
            continue
        attempts -= 1
        print('Этой буквы нет в слове\nПроверенные буквы:', tried_letters)
    if attempts:
        print('\n   .•*°*•.✿.•°*Вы победили!*°•.✿.•*°*•.\n о/ \n/|\n/ \ \n')
    else:
        print(' _____\n |/  |\n |   o\n |  /|\ \n |  / \ \n |\n | попытки закончились, вы проиграли\nЗагаданное слово:', slovo)
    main()

def main():
    game = input('Если хотите сыграть - введите да, если не хотите - любой другой символ\n')
    if game.lower() == 'да':
        igra(get_a_word())
    else:
        print('До новых встреч!!! =^･ｪ･^=')
       
if __name__ == '__main__':
    main()

#   °*•.✿.•*°*•. Вы победили .•*°*•.✿.•*°
#                *•.     .•*
#                    \о/
#                     |
#                    / \
