# ЗАДАЧИ К СЕМИНАРУ 3
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# import random
# list = []
# count = 0
# for i in range(10):
#     list.append(random.randint(0,9))
#     if i%2 !=0:
#         count+=list[i]
# print(f'Наш получившийся список: {list}')
# print(f'Cумма элементов с нечетных позиций: {count}')

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# import random
# list = []
# count = []
# for i in range(random.randint(3,15)):
#     list.append(random.randint(0,9))
# len1 = len(list)/2
# if len1%2 != 0:
#     len1+=0.5
# len1=int(len1)   
# for i in range(1,len1+1):
#     count.append(list[i-1]*list[-i])
# print(len1)
# print(f'Первый список: {list}')
# print(f'Получившееся произведение: {count}')


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# import random
# list = []
# for i in range(random.randint(3,9)):
#     list.append(round(random.random()*100,2))
# list2 = []
# for i in range(len(list)):
#     if list[i] != int(list[i]):
#         list2.append(round(list[i]-int(list[i]), 2))
   
# count = max(list2)-min(list2)

# print(f'наш получившийся список: {list}')
# print(f'разница max и min дробных частей: {round(count, 2)}')


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# num = int(input('Введите число: '))
# num2 = []
# while num>0:
#     if num%2 == 0:
#         num2.append(0)
#     else:
#          num2.append(1)
#     num= num//2
# num2.reverse() 
# print(f'В двочиной системе число {num} будет выглядеть так: ', end = " ")
# print(*num2)

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
# num = int(input('Введите число: '))
# fib_list = [1, 0, 1]
# if num>1:
#     for i in range (1, num):
#         fib_list.append(fib_list[i+1] +fib_list[i])
#     for i in range (1, num):
#         fib_list.insert(0, (fib_list[1] -fib_list[0]))
# print(fib_list)

