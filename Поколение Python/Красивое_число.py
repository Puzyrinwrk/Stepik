"""
Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17. Напишите программу,
определяющую, является ли введённое число красивым. Программа должна вывести «YES», если число является красивым,
или «NO» в противном случае.

Формат входных данных
На вход программе подаётся натуральное число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

1043
Sample Output 1:

YES
Sample Input 2:

1045
Sample Output 2:

NO
Sample Input 3:

2751
Sample Output 3:

YES
"""

n = int(input())
if (999 < n < 10000) and (n % 7 == 0 or n % 17 == 0):
    print('YES')
else:
    print('NO')
