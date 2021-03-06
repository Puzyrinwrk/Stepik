"""
Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.

Формат входных данных
На вход программе подается четыре вещественных числа, каждое на отдельной строк.

Формат выходных данных
Программа должна вывести одно число – евклидово расстояние.

Sample Input 1:

2.0
2.5
44.155
100.50
Sample Output 1:

106.68197610187018
"""

from math import *

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(sqrt(((x1 - x2)**2) + ((y1 - y2)**2)))
