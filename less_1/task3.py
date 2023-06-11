

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 100
ATTEMPTS = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range (ATTEMPTS):
    user_num = int(input('Угадай число, которое я загадал '))
    if user_num == num:
        print('Молодец! Угадал!')
        break
    elif user_num > num:
        print('Неверно, но меньше')
    elif user_num < num:
        print('Неверно, но больше')
else:
    print('Попытки закончились! ')
