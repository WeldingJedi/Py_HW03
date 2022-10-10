def task01():
    # Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.

    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # day = int(input('Enter a weekday number: '))  # можно ручками, а можно автоматизировать =)
    import random
    day = random.randint(-1, 9)
    print(day)
    if day in range(1, 8):
        print(week[day - 1])
    else:
        print('This day does not exist')


def task02():
    # Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

    import random
    x1 = random.randint(-10, 10)
    y1 = random.randint(-10, 10)
    print(f'1st point coordinates: ({x1}, {y1})')
    x2 = random.randint(-10, 10)
    y2 = random.randint(-10, 10)
    print(f'2nd point coordinates: ({x2}, {y2})')
    dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5   # или math.sqrt и pow можно использовать
    print(f'Distance between 1st point and 2nd: {dist}')


def task03():
    # Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
    # точек в этой четверти (x и y).
    import random
    quarter = random.randint(1, 4)
    print(f'Chosen quarter is {quarter}')
    if quarter == 1:
        print(f'Range of X and Y coordinates in a quarter {quarter}: 0 to {chr(126)}')  # взял тильду за самый близкий к знаку бесконечности
    elif quarter == 2:
        print(f'Range of X coordinates in a quarter {quarter}: 0 to {chr(126)}')
        print(f'Range of Y coordinates in a quarter {quarter}: 0 to -{chr(126)}')
    elif quarter == 3:
        print(f'Range of X and Y coordinates in a quarter {quarter}: 0 to -{chr(126)}')
    else:
        print(f'Range of X coordinates in a quarter {quarter}: 0 to -{chr(126)}')
        print(f'Range of Y coordinates in a quarter {quarter}: 0 to {chr(126)}')


def task04():
    # Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
    import random
    number = random.randint(1, 100)
    print(f'Selected {number}')
    start = 1
    while start <= number:
        if start % 2 == 0:
            print(start, end = " ")
            start += 1
        else:
            start += 1


# task01()
# task02()
# task03()
# task04()
