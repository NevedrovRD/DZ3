# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.


n = int(input("Введите десятичное число ")) 
y = n
x = ""

while n > 0:
    x = str(n % 2) + x
    n = n // 2

print(f"{y} в двоичном виде равно => {x}")