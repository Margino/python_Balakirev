# Подвиг 4. На вход программе подается целое число: порядковый номер дня недели (1, 2, ..., 7). Необходимо прочитать это число и вывести на экран название дня недели:

# понедельник, вторник, среда, четверг, пятница, суббота, воскресенье

# Программу реализовать с использованием операторов if-elif.

days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

num = int(input('Введите число:'))

if num < 1:
    print('Вы указали некорректное число!')
else:
    if num <= 7:
        day_index = num - 1
    else:
        remainder = num % 7
        if remainder == 0:
            day_index = 6
        else:
            day_index = remainder - 1

    if day_index == 0:
        print(days[day_index])
    elif day_index == 1:
        print(days[day_index])
    elif day_index == 2:
        print(days[day_index])
    elif day_index == 3:
        print(days[day_index])
    elif day_index == 4:
        print(days[day_index])
    elif day_index == 5:
        print(days[day_index])
    else:
        print(days[day_index])
