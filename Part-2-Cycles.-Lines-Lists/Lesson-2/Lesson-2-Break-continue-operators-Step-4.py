# Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
#
# Для каждого введённого числа проверить:
# если число меньше 10, то пропускаем это число;
# если число больше 100, то прекращаем считывать числа;
# в остальных случаях вывести это число обратно на консоль в отдельной строке.
#
# Sample Input 1:
# 12
# 4
# 2
# 58
# 112
#
# Sample Output 1:
# 12
# 58
#
# Sample Input 2:
# 101
#
# Sample Output 2:
# None
#
# Sample Input 3:
# 1
# 2
# 102
#
# Sample Output 3:
# None


n = 0
while n < 101:
    n = int(input())
    if n < 10:
        continue
    elif n > 100:
        break
    else:
        print(n)
