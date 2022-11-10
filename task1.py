# Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.

number = 132
number = str(number)
n = number + number
m = number + number + number
sum = int(number) + int(n) + int(m)
print(f'N + NN + NNN = {number} + {n} + {m} = {sum}')