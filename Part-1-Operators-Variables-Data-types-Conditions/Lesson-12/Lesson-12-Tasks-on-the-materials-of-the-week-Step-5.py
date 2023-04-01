# Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
#
# На ввод могут подаваться и повторяющиеся числа.
#
# Sample Input 1:
# 8
# 2
# 14
#
# Sample Output 1:
# 14
# 2
# 8
#
# Sample Input 2:
# 23
# 23
# 21
#
# Sample Output 2:
# 23
# 21
# 23


'''
выводим на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
'''

a = int(input())
b = int(input())
c = int(input())
if (a >= b and a >= c) and a >= b >= c:
    print(a)
    print(c)
    print(b)
elif (a >= b and a >= c) and a >= c >= b:
    print(a)
    print(b)
    print(c)
elif (b >= a and b >= c) and b >= a >= c:
    print(b)
    print(c)
    print(a)
elif (b >= a and b >= c) and b >= c >= a:
    print(b)
    print(a)
    print(c)
elif (c >= a and c >= b) and c >= a >= b:
    print(c)
    print(b)
    print(a)
elif (c >= b and c >= a) and c >= b >= a:
    print(c)
    print(a)
    print(b)
