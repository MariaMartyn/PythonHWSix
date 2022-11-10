# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.


def fareiRow(n, row = True):
    if row:
        a, b, c, d = 0, 1, 1, n
    else:
        a, b, c, d = 1, 1, n-1, n
    print ('%d / %d' % (a, b))

    while (row and c <= n) or (not row and a > 0):
        m = int ((n + b) / d)
        a, b, c, d = c, d, m*c - a, m*d - b
        print ('%d / %d' % (a, b))
print('Простые несократимые дроби: ')
fareiRow(11)
