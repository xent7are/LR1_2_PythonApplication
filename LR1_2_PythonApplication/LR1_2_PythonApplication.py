# -*- coding: cp1251 -*-

# Программа, которая генерирует список элементов случайным образом из диапазона от 5 до 14*10.
# Количество элементов в списке 14+10.

import random

# Номер по журналу
journal_number = 14

# Минимальное значение в списке
min_value_in_list = 5
# Максимальное значение в списке (14 * 100 = 1400)
max_value_in_list = journal_number * 100
# Число элементов в списке (14 + 10 = 24)
element_count = journal_number + 10

# Создание пустого списка
random_list = []

# Функция, которая генерирует список случайных чисел в заданном диапазоне значений и количеством элементов
def generate_random_list(min_value_in_list, max_value_in_list, element_count):
    # Генерация элементов
    for i in range(element_count):
        # Добавление в список случайного числа от 5 до 1400
        random_list.append(random.randint(min_value_in_list, max_value_in_list))

    return random_list

# Вывод результата
print("Сгенерированный список: ", generate_random_list(min_value_in_list, max_value_in_list, element_count))
