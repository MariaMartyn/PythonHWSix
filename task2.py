# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, 
# совпадающая с введённым числом.

import random
numbers = [random.randint(1, 9) for i in range(15)]
print(numbers)
number = int(input('Введите трехзначное число: '))
print(number)

number = str(number)
numbers = str(numbers)
numbers = numbers.replace(',', '')
numbers = numbers.replace(' ', '')
   
count = 0
i = 1
while i <= len(numbers):
    if number == numbers[i : i + 3]:
        i +=1
        count += 1
    else:
        i+=1

print('Да, в массиве есть такая последовательность элементов' if count> 0 else 'Нет, в массиве нет такой последовательности элементов')      


       
