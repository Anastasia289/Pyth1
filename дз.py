# ЗАДАЧИ К СЕМИНАРУ 4 

# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k1 = int(input('Введите натуральную степень для уравнения 1: '))
k2 = int(input('Введите натуральную степень для уравнения 2: '))
# k1 = 3 
# k2 = 2


def eq (k: int):
    eqq = []
    kk = k
    for i in range(k):
        temp = random.randint(-100, 100)
        if temp == 0:
            if k==kk:
                eqq.append(f'x**{k}')
                k-=1
            elif k!=kk and k!=0:
                k-=1
        elif temp == 1:
            eqq.append(f'x**{k}')
            k-=1
        elif temp == -1:
            eqq.append(f'-x**{k}')
            k-=1
        else:
            if k > 1:
                eqq.append(f'{temp}*x**{k}')
                k-=1 
            if k == 0:
                eqq.append(f'{temp}')
                break
            if k == 1:
                eqq.append(f'{random.randint(-100, 100)}*x')
                k-=1            
      
    return eqq

def conv (eq1: list):
    eq11 = ''
    for el in eq1:
        if el == eq1[len(eq1)-1]:
            eq11 += str(f'{el} = 0') 
            break
        else:
            eq11 += str(f'{el} + ')
        
    eq11 = eq11.replace('+ -', ' - ')  
    return eq11

eq1 = eq(k1)
eq2 = eq(k2)
eq11 = conv(eq1)
eq22 = conv(eq2)

print(f'Первое уравнение: {eq11}')
print(f'Второе уравнение: {eq22}')

# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий 
# сумму многочленов.

# print(f'ПервЫЙ многочлен в виде списка: {eq1}')
# print(f'Второй многочлен в виде списка: {eq2}')

def Create_dict (eq: list):
    dict = {}
    for el in eq:
        if '**' in el:
            if '*x**' in el:
                el = el.split('*x**')
                dict[int(el[1])] = int(el[0])
            else:
                el = el.split('x**')
                if el[0] == '-':
                    dict[int(el[1])] = int(-1)  
                else:
                    dict[int(el[1])] = int(1) 
        elif 'x' in el and "**" not in el:
            el = el.split('*x')
            dict[1] = int(el[0])
        else:
            dict[0] = int(el)
    return dict

def Combine (dict1: dict, dict2: dict):
    keys = set()
    for key in dict1:
        keys.add(key)
    for key in dict2:
        keys.add(key)
    for key in keys:
        dict1[key] = dict1.get(key,0) + dict2.get(key,0) 
    return dict1


dict1 = Create_dict (eq1)
dict2 = Create_dict (eq2)
# print(f'словарь1: {dict1}')
# print(f'словарь2: {dict2}')
dict1 = Combine (dict1, dict2)
# print(f'словарь новый: {dict1}')
        
a = []
b = []
for key in dict1:
        a.append(key)
a.sort(reverse=True)

for el in a:
    if el == 0:
        b.append(dict1[el])
        break
    if el == 1:
        if dict1[el] !=0:
            if dict1[el] == 1:
                b.append('x')
            if dict1[el] == -1:
                b.append('-x')
            else:
                b.append(f'{dict1[el]}*x')
    else:
        if dict1[el] !=0:
            if dict1[el] == 1:
                b.append(f'x**{el}')
            elif dict1[el] == -1:
                b.append(f'-x**{el}')
            else:
                b.append(f'{dict1[el]}*x**{el}')
b = conv(b)
print(f'Cумма многочленов равна: {b}')
    