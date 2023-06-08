# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
A=[]
k = 0
n = int(input("Введите количество элементов массива: "))
for i in range(n):
    A.append(random.randrange(100))
BeginRange = int(input("Введите начало диапазона: "))
EndRange = int(input("Введите конец диапазона: "))
print(*A)
for i in range(n):
    if BeginRange <= A[i] <= EndRange:
        print(i)
        k +=1
if k == 0:
    print(f"В диапазоне {BeginRange} : {EndRange} нет элементов массива")