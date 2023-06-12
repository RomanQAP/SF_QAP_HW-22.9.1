# создаем алгоритм "быстрой" сортировки

import random


def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)

    return array


# создаем алгоритм "двоичного" поиска
def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle - 1
    elif element < array[middle]:

        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


string = input('Введите последовательность натуральных чисел через пробел:')
string_split = string.split()
# Отлавливаем ошибку в случае неверных типов данных и останавливаем программу.
try:
    numbers = list(map(int, string_split))
except ValueError as VE:
    print('Неверные данные, проверьте, что вы ввели натуральные числа и перезапустите программу!')
else:
    # Создаю переменные для ввода в аргументы при вызове функций.
    left = 0
    right = len(numbers) - 1
    numbers_sort = qsort_random(numbers, left, right)
    print('Ваша отсортированная последовательность:', numbers_sort)

    # Отлавливаем ошибку в случае неверных типов данных и останавливаем программу.
    try:
        num = int(input('Введите натуральное число: '))
    except ValueError as VE:
        print('Неверные данные, проверьте, что вы ввели натуральное число и перезапустите программу!')
    else:
        # Отлавливаем ошибку в случае отсутствия числа в последовательности.
        try:
            if numbers.index(num):
                print('Ваше число имеется в списке.')

        except ValueError as VE:
            print('Число не найдено!')

        else:
            print('Позиция левого элемента от вашего числа:', binary_search(numbers, num, left, right))
