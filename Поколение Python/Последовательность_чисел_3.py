"""
Даны два целых числа m и n (m > n). Напишите программу, которая выводит все нечетные числа от m до n включительно
в порядке убывания.

Формат входных данных
На вход программе подаются два целых числа m и n, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести числа в соответствии с условием задачи.

Примечание. Попробуйте решить задачу двумя способами: с использованием условного оператора if и без него.

Sample Input 1:

77
62
Sample Output 1:

77
75
73
71
69
67
65
63
"""

m = int(input())
n = int(input())

for i in range(m, n - 1, -1):
    if i % 2 != 0:
        print(i)
