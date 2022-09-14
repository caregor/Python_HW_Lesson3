""""
1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
    - [2, 3, 4, 5, 6] => [12, 15, 16];
    - [2, 3, 5, 6] => [12, 15]
3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
значением дробной части элементов.
    Пример:
    - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    Пример:
    - 45 -> 101101
    - 3 -> 11
    - 2 -> 10
5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    Пример:
    - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""


# Задача №1
# CONST_LIST = [2, 3, 5, 9, 9]
# odd_list = [CONST_LIST[n] for n in range(1, len(CONST_LIST), 2)]
# print(sum(odd_list))

# Задача №2
# data_list = list(map(int, input('Enter some list: ').split()))
# result = []
# while data_list:
#     try:
#         first = data_list.pop(0)
#         last = data_list.pop()
#     except:
#         result.append(first * first)
#         break
#     result.append(first * last)
# print(result)

# Задача №3
# data = [1.1, 1.2, 3.1, 5.1, 10.01]
# tmp_list = []
# for i in range(len(data)):
#     tmp_list.append(data[i] * 100 % 100)
# print((max(tmp_list) - min(tmp_list)) / 100)

# Задача №4
# def dec_to_bin(number):
#     if number > 1:
#         dec_to_bin(number // 2)
#     print(number % 2, end='')
#
#
# some_number = int(input('Enter a Dec number: '))
# dec_to_bin(some_number)
# print()
# # с помощью готовой функции
# print(bin(some_number).replace('0b',''))

# Задача №5
k = int(input('k = '))
tmp = 0
result = []
fibonacchi = [0, 1]
for i in range(k - 1):
    tmp = fibonacchi[i] + fibonacchi[i+1]
    fibonacchi.append(tmp)
    if i % 2 == 0:
        result.append(-tmp)
    else:
        result.append(tmp)
result.reverse()
result.extend(fibonacchi)
print(result)