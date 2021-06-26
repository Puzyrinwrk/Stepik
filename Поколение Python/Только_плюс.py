"""
Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

Формат входных данных
На вход программе подаются три целых числа.

Формат выходных данных
Программа должна вывести одно число – сумму положительных чисел.

Примечание. Если положительных чисел нет, то следует вывести 00.

Sample Input 1:

4
-22
1
Sample Output 1:

5
Sample Input 2:

33
55
63
Sample Output 2:

151
Sample Input 3:

-1
37
62
Sample Output 3:

99
"""

a = int(input())
b = int(input())
c = int(input())
if a > 0 and b > 0 and c > 0:
    print(abs(a + b + c))
elif a > 0 and b > 0 and c < 0:
    print(abs(a + b))
elif a > 0 and b < 0 and c > 0:
    print(abs(a + c))
elif a < 0 and b > 0 and c > 0:
    print(abs(b + c))
elif a < 0 and b < 0 and c > 0:
    print(abs(c))
elif a > 0 and b < 0 and c < 0:
    print(abs(a))
elif a < 0 and b > 0 and c < 0:
    print(abs(b))
else:
    print(0)
