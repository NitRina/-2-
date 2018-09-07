#dppopova@hse.ru
#daschapopowa@gmail.com

import random

array = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
array = list(array)
x = random.choice(array)
letter = input('Угадайте загаданную букву латинского алфавита ')
if letter in array:
    if letter == x:
        print('вы угадали')
    else:
        print('вы не угадали, загаданная буква', x)

else:
    print('это не буква латинского алфавита')
    
