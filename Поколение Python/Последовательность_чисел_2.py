"""
Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n включительно в порядке возрастания,
если m < n, или в порядке убывания в противном случае.

Формат входных данных
На вход программе подаются два целых числа m и n, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести числа в соответствии с условием задачи.

Sample Input 1:

1
5
Sample Output 1:

1
2
3
4
5
"""

m = int(input())
n = int(input())

for i in range(m, n + 1):
    if m < n:
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)
