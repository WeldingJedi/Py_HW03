def square_num():
    # 0. Напишите программу, которая на вход принимает число и выдаёт его квадрат (число умноженное на само себя).

    number = input('Enter number: ')
    number = int(number)
    print(f"{number} * {number} = {number ** 2}")


def check_square():
    # 1. Напишите программу, которая на вход принимает два числа и проверяет, является ли одно число квадратом другого.

    number1 = int(input('Enter 1st integer: '))
    number2 = int(input('Enter 2nd integer: '))

    if number2 == number1 * number1 or number1 == number2 * number2:
        print('Yes')
    else:
        print('No')


def serial_input_multiple_of_3():
    #  2. Организуйте последовательный ввод чисел до тех пор, пока не будет введён 0. 
    # Подсчитайте среди введённых чисел те, которые кратны трём.

    import random
    number = None
    count = 0
    while number != 0:
        number = random.randint(-10, 10)
        if number != 0 and number % 3 == 0:
            count += 1
        print(number, end = " ")
    print(f'\nZero detected and integers multiple of 3: {count}')


def print_range():
    # 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N 
    # 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

    number = int(input('Enter integer for range: '))
    print(*range(-number, number + 1))


def fractional_part():
    # 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа. 
    # 6,78 -> 7 5 -> нет 0,34 -> 3

    number = float(input('Enter number: '))
    if round(number, 0) == number:
        print('There is no any fractional part')
    else:
        print(f'{int(number * 10 % 10)}')


def max_min_list():
    # 5. Напишите программу, которая находит наибольшее и наименьшее число из списка значений
    
    import random
    # size = int(input('Enter size of the list: '))
    size = random.randint(3, 9)
    array = [None] * size
    for i in range(size):
        array[i] = random.randint(-10, 10)
        # print(f'[{array[i]}]', end = " ")
    print(array)
    print(f'\nMax element is [{max(array)}], min element is [{min(array)}]')
    

def sum_of_3digs_multiple_of_3():
    # Задача 2. Дано трёхзначное число N. Определить кратна ли трём сумма всех его цифр.

    import random
    number = random.randint(100, 999)
    print(f'Selected number is {number}')
    ones = number % 10
    tens = number // 10 % 10
    hund = number // 100
    if (ones + tens + hund) % 3 == 0:
        print(f'{number} is multiple of 3')
    else:
        print(f'Sorry, {number} is not multiple of 3')


def finding_4_or_7_in_number():
    # Задача 3. Дано трёхзначное число N. Определить, есть ли среди его цифр 4 или 7.
    import random
    number = random.randint(100, 999)
    print(f'Selected number to determine the dig 4 or 7 in its composition is {number}')
    hund = number // 100
    tens = number // 10 % 10
    ones = number % 10
    if ones == 4 or ones == 7 or tens == 4 or tens == 7 or hund == 4 or hund == 7:
        print('You got it')
    else:
        print('Nope')


def sequential_array_10():
    # Задача 4. Дан массив длиной 10 элементов. Заполнить его последовательно числами от 1 до 10.

    size = 10
    array = [None] * size
    for i in range(size):
        array[i] = i + 1
        # print(f'[{array[i]}]', end = " ")
    print(array)


def array_0_1_length_1square():
    # Задача 2. Напишите метод, который заполняет массив случайным количеством (от 1 до 100) нулей и единиц. 
    # Размер массива должен совпадать с квадратом количества единиц в нём.

    import random
    leng = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    size = random.randint(1, len(leng) - 1)
    array = [0] * leng[size]
    count1 = leng[size]**0.5
    while count1 > 0:
        i = random.randint(0, leng[size] - 1)
        if array[i] != 1:
            array[i] = 1
            count1 -= 1
    print(array)
    print(f'Array size: {leng[size]}, quantity of [1]: {int(leng[size]**0.5)} ')


def digs_sequence_in_array():
    # Задача 1. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. 
    # Напишите программу, которая определяет, есть в массиве 
    # последовательность из трёх элементов, совпадающая с введённым числом.
    # {0, 5, 6, 2, 7, 7, 8, 1, 1, 9} - 277 -> да
    # {4, 4, 3, 6, 7, 0, 8, 5, 1, 2} - 812 -> нет

    import random
    number = random.randint(100, 999)
    print(f'Selected number: {number}')
    hund = number // 100
    tens = number // 10 % 10
    ones = number % 10
    count = 0
    size = 15
    array = [None] * size
    for i in range(size):
        array[i] = random.randint(0, 9)
        print(f'[{array[i]}]', end = " ")
    # print(array)
    for i in range(0, size - 2):
        if array[i] == hund and array[i + 1] == tens and array[i + 2] == ones:
            count += 1
    if count > 0: print('\nYeah!')
    else: print('\nNope')
            

# square_num()
# check_square()
# serial_input_multiple_of_3()
# print_range()
# fractional_part()
# max_min_list()
# sum_of_3digs_multiple_of_3()
# finding_4_or_7_in_number()
# sequential_array_10()
# array_0_1_length_1square()
# digs_sequence_in_array()
