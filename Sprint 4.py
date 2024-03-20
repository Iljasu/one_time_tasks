# def main():
#     a = int(input())
#     b = int(input())
#     c = a + b
#     print(c)


# if __name__ == '__main__':
#     main()


# # name.py

# name = input('Как тебя зовут?\n')
# print(f'Привет, {name}!')


# # name.py

# import sys

# name = sys.stdin.readline()  # Применим readline().
# print(f'Привет, {name}!')


# # name.py

# import sys

# name = sys.stdin.readline().rstrip()
# print(f'Привет, {name}!')

# def check_element_in_list(desired_element, ordered_list):
#     """Проверяет наличие искомого элемента в отсортированном списке."""
#     for item in ordered_list:
#         if item < desired_element:
#             continue
#         elif item == desired_element:
#             return f'Элемент {desired_element} найден в массиве!'
#         elif item > desired_element:
#             break
#     return f'Элемент {desired_element} не найден в массиве.'


# # Вызываем функцию с тестовыми данными.
# # Первый аргумент - целое число.
# # Второй аргумент - отсортированный по возрастанию список целых чисел.
# result = check_element_in_list(8, [1, 3, 5, 7, 10])
# # Распечатываем результат.
# print(result)

# for i in range(1,15):
#     print(4**i, '   степень - ', i)


# example_array = [6, 5, 3, 1, 8, 7, 2, 4]


# def bubble_sort(data):
#     # Напишите здесь код сортировки.

#     last_index = len(data) - 1
#     swapped = True

#     while swapped:

#         swapped = False

#         for item_index in range(0, last_index):

#             if data[item_index] > data[item_index + 1]:
#                 data[item_index], data[item_index + 1] = (
#                     data[item_index + 1], data[item_index])
#                 swapped = True

#         last_index -= 1

#     return data


# print(bubble_sort(example_array))


# def list_superset(list_set_1, list_set_2):
#     # Не меняйте названия функции и параметров. Напишите решение здесь.
#     count = 0
#     result = None
#     if len(list_set_1) >= len(list_set_2):
#         for i in range(len(list_set_2)):
#             if list_set_2[i] in list_set_1:
#                 count += 1
#         if count == len(list_set_2) and len(list_set_1) != len(list_set_2):
#             result = f'Набор {list_set_1} - супермножество.'
#         elif count != len(list_set_2):
#             result = 'Супермножество не обнаружено.'
#         elif count == len(list_set_2) and len(list_set_1) == len(list_set_2):
#             result = 'Наборы равны.'
#     count = 0
#     if len(list_set_1) <= len(list_set_2):
#         for i in range(len(list_set_1)):
#             if list_set_1[i] in list_set_2:
#                 count += 1
#         if count == len(list_set_1) and len(list_set_1) != len(list_set_2):
#             result = f'Набор {list_set_2} - супермножество.'
#         elif count != len(list_set_1):
#             result = 'Супермножество не обнаружено.'
#         elif count == len(list_set_1) and len(list_set_1) == len(list_set_2):
#             result = 'Наборы равны.'
#     return result


# # Примеры для проверки функции.
# list_set_1 = [1, 3, 5, 7]
# list_set_2 = [3, 5]
# list_set_3 = [5, 3, 7, 1]
# list_set_4 = [5, 6]

# print(list_superset(list_set_1, list_set_2))
# print(list_superset(list_set_2, list_set_3))
# print(list_superset(list_set_1, list_set_3))
# print(list_superset(list_set_2, list_set_4))


# # Импорт библиотеки для работы с временем.
# import time

# # Количество элементов в массивах.
# elements_count = 10000000

# # Эксперимент 1
# # Засекаем время начала.
# start_time = time.time()
# # Резервируем место в памяти на 10 млн элементов.
# # При этом ОС забронирует чуть больший размер.
# data1 = [None] * elements_count
# for data_index in range(elements_count):
#     # Заполняем элементы списка по индексу.
#     data1[data_index] = f'Some new value {data_index}'
# # Печатаем время выполнения.
# print(
#     'Создание списка с 10 млн пустых элементов и его заполнение:', 
#     time.time() - start_time
# )

# # Эксперимент 2
# # Засекаем новое время.
# start_time = time.time()
# # Объявляем пустой список; ОС не знает его ожидаемый размер.
# data2 = []
# for data_index in range(elements_count):
#     # Добавляем новые элементы в конец списка.
#     data2.append(f'some new value {data_index}')
# # Печатаем время выполнения.
# print(
#     'Создание пустого списка и добавление в него 10 млн элементов:', 
#     time.time() - start_time
# )


from array import array

from sys import maxsize


def valid_mountain_array():
    elements_data = input().split()
    print(elements_data)
    first_array = array('b', elements_data)

    index_max_element = first_array.index[max(elements_data)]
    print(index_max_element)


valid_mountain_array()
