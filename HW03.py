# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

def task01():

    n = int(input('Enter Fibonacci sequence length: '))
    fib1 = 0
    fib2 = 1
    data = open('fibonacci.txt', 'w')
    for _ in range(n):
        print(fib1, end = ' ')
        data.writelines(str(fib1) + '\n')
        (fib1, fib2) = (fib2, fib1 + fib2)
    data.close()

# task01()


# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

def task02():
    
    data = open('fruits.txt', encoding = 'utf-8')
    fruits = data.readline().split()
    sym = input('Enter 1st symbol of fruit lowercase, please: ')
    for ifruct in fruits:
        if ifruct[0] == sym.upper():
            print(ifruct)
    data.close()

# task02()


# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет»,
# «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу. «как тебя зовут?» –> меня зовут Анатолий

def task03():
    dictionary = \
        {
            'Привет': 'Шалом',
            'Как тебя зовут?': 'Меня зовут БОТ7000',
            'Как дела?': 'Хорошо было, пока ты не спросил',
            'Почему?': 'Потому что!',
            'Пока': 'Адьё, кожаный'
        }

    is_started = True
    while is_started:
        answer = input('Я: ')
        if answer == 'Выход':
            is_started = not is_started
        if answer in dictionary.keys():
            print('Бот:', dictionary[answer])
        else:
            print('10101011101110110101111011101101111111011111011101000001100011110111111011011101101110000111011101100100')
            # Unknown command in binary
            break

# task03()