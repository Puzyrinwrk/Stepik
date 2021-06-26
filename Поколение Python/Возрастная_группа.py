"""
Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:

до 13 включительно – детство;
от 14 до 24 – молодость;
от 25 до 59 – зрелость;
от 60 – старость.
Формат входных данных
На вход программе подаётся одно целое число – возраст пользователя.

Формат выходных данных
Программа должна вывести название возрастной группы.

Sample Input 1:

4
Sample Output 1:

детство
Sample Input 2:

91
Sample Output 2:

старость
Sample Input 3:

40
Sample Output 3:

зрелость
"""

age = int(input())
if age <= 13:
    print('детство')
elif 14 <= age <= 24:
    print('молодость')
elif 25 <= age <= 59:
    print('зрелость')
else:
    print('старость')
