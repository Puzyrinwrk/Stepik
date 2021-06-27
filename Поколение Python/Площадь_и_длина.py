"""
Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.

Формат входных данных
На вход программе подается одно вещественное число R.

Формат выходных данных
Программа должна вывести два числа – площадь круга и длину окружности радиуса R.

Примечание. Используйте константу math.pi.

Sample Input 1:

554.6
Sample Output 1:

966294.7126386268
3484.654571361799
"""

from math import *

r = float(input())
print(pi * r ** 2)
print(2 * pi * r)
