"""
Напишите программу вывода на экран трех последовательно идущих чисел, каждое на отдельной строке. Первое число
вводит пользователь, остальные числа вычисляются в программе.

Формат входных данных
На вход программе подается одно целое число.

Формат выходных данных
Программа должна вывести три последовательно идущих числа в соответствии с условием задачи.

Sample Input 1:

8
Sample Output 1:

8
9
10
"""

n = int(input())
print(n, n + 1, n + 2, sep='\n')
