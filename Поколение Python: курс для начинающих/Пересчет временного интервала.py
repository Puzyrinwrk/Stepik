"""
Напишите программу для пересчёта величины временного интервала, заданного в минутах, в величину, выраженную в
часах и минутах.

Формат входных данных
На вход программе подаётся целое число – количество минут.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

150
Sample Output 1:

150 мин - это 2 час 30 минут.
"""

minute = int(input())  # Количество минут
print(f'{minute} мин - это {minute // 60} час {minute % 60} минут. ')

