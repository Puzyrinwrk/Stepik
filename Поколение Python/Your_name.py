"""
Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:

«Hello [введенное имя] [введенная фамилия]! You just delved into Python».

Формат входных данных
На вход программе подаётся две строки (имя и фамилия), каждая на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Между firstname lastname вставьте пробел =)

Sample Input 1:

Anthony
Joshua
Sample Output 1:

Hello Anthony Joshua! You just delved into Python
"""

name = input()
lastname = input()
print(f'Hello {name} {lastname}! You just delved into Python')

