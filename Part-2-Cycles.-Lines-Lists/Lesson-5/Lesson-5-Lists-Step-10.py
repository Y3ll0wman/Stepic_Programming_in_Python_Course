# Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.
#
# Используйте метод split строки.
#
# Sample Input:
# 4 -1 9 3
#
# Sample Output:
# 15


a = [int(i) for i in input().split()]
a_len = len(a)
sum = 0
for i in a:
    sum = sum + i
print(sum)
