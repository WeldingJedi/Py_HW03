# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def task01():       # факториал while
    n = int(input('Enter integer: '))
    for i in range(1, n + 1):
        factorial = 1
           
        while i > 1:
            factorial *= i
            i -= 1
        print(f'[{factorial}]', end = " ")

# task01()

def task01_1():     # факториал for
    n = int(input('Enter integer: '))
    for i in range(1, n + 1):
        factorial = 1
        for j in range(2, i + 1):
            factorial *= j
        print(f'[{factorial}]', end = " ")

# task01_1()

def task01_2(x):    # факториал рекурсией
    if x == 0:
        return 1
    return task01_2(x - 1) * x

def task01_2_1():
    n = int(input('Enter integer: '))
    for i in range(1, n + 1):
        print(f'{[task01_2(i)]}', end = " ")

# task01_2_1()

def task01_3():     # факториал math
    import math
    n = int(input('Enter integer: '))
    for i in range(1, n + 1):
        print(f'{[math.factorial(i)]}', end = " ")

# task01_3()


# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def task02():

    print('| X | Y | Z | XYZ')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                res = not(x and y) or z     # мне кажется, что я не совсем верно понял математическое выражение
                print(f'| {x} | {y} | {z} | {int(res)} |')

# task02()


# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def task03():
    str1 = input('Enter short string: ')
    str2 = input('Enter long string: ')
    if str1 >= str2:
        print('Please, read more attentively!')
    print('Short string symbols contains in long string:')
    for i in range(len(str1)):
        print(f'"{str1[i]}" - {str2.count(str1[i])} time(s)')

# task03()


# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def task04():

    number = int(input('Enter integer for range: '))
    size = number * 2 + 1
    array = [None] * size
    for i in range(size):
        array[i] = -number + i
    print(f'Origianl array:\n{array}')
    print(f'Array with elements shifted to the right by 2 positions:\n{array[-2:] + array[:-2]}')

# task04()