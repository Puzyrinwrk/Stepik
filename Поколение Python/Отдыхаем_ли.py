"""
Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке есть
подстрока «суббота» или «воскресенье», и «NO» в противном случае.

Формат входных данных
На вход программе подается одна строка.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

Какой сегодня день недели?
Sample Output 1:

NO
Sample Input 2:

Была суббота, и ему хотелось поскорее уехать домой.
Sample Output 2:

YES
Sample Input 3:

День в воскресенье выдался тёплым и солнечным.
Sample Output 3:

YES
"""

a = input()
if 'суббота' in a or 'воскресенье' in a:
    print('YES')
else:
    print('NO')

