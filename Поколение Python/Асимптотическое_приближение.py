"""
На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения
....
Примечание. Для вычисления натурального логарифма воспользуйтесь функцией log(n), которая находится в модуле math.

Sample Input 1:

10
Sample Output 1:

0.6263831609742079
Sample Input 2:

1
Sample Output 2:

1.0
Sample Input 3:

100
Sample Output 3:

0.5822073316515288
"""

from math import *

n = int(input())
s = 0
for i in range(1, n + 1):
    s += 1 / i
num = s - log(n)
print(num)
