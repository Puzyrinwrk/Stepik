"""
Напишите программу, которая считает стоимость трех компьютеров, состоящих из монитора, системного блока,
клавиатуры и мыши.

Формат входных данных На вход программе подаётся четыре целых числа, каждое на отдельной строке. В первой строке —
стоимость монитора, во второй строке — стоимость системного блока, в третьей строке — стоимость клавиатуры и в
четвертой строке — стоимость мыши.

Формат выходных данных
Программа должна вывести одно число – стоимость покупки (трех компьютеров).

Sample Input 1:

9900
55600
3999
2990
Sample Output 1:

217467
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(3 * (a + b + c + d))
