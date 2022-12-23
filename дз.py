# Семинар 2

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:6782 -> 23
# 0,56 -> 11

num = float(input('Введите число:_ '))
c=0
count = 0
if num != int(num):
    num2 = str(num)
    num2 = num2.split(".")
    c = len(num2[1])
if c != 0:
    num *=10**c
num = int(num)
while (num != 0): 
    count = count + num % 10 # вроде работает, но как-то не изящно :( Как сделать рациональнее?
    num = num // 10

print(count)

# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input("Введите число:  "))
row = []
count = 0
for i in range(1,n+1):
    temp = round((1 + 1/i)**i,2)
    row.append(temp)
    count += temp
print(f'При n= {n}: ', end = ' ') 
print(*row, sep = ', ') 
print(f'Cумма чисел списка равна: {count}') 

# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int
import random

list= 'Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE'
list = list.split(" ")

for i in range(len(list)):
    i_temp = random.randint(0, len(list)-1) # вариант с текстом
    temp = list[i_temp]
    list[i_temp] = list[i]
    list[i] = temp
print(f'Тадам:  {list}')


