# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randrange


x = int(input('Количество элементов списка '))

list = []
list1 = []

for i in range(x):
    list.append(randrange(0, 99))

for i in range(len(list)):
    while i < len(list)/2 and x > len(list)/2:
        x -= 1
        n = list[i] * list[x]
        list1.append(n)
        i += 1



print(f"{list} => {list1}")