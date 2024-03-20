# import time


# def sleep_one_sec():
#     print('Функция sleep_one_sec() начала вычисления.')
#     print('Вычисляю...')
#     time.sleep(1)
#     return 'Функция sleep_one_sec() завершила вычисления.'


# def time_of_function(func):
#     def wrapper():
#         start_time = time.time()
#         print('Время пошло')
#         result = func()
#         execution_time = round(time.time() - start_time, 3)
#         print(f'Через {execution_time} сек. функция вернула «{result}»')
#         return result
#     return wrapper


# result = time_of_function(sleep_one_sec)
# print(result)

ls = [3] * 5
print(ls)