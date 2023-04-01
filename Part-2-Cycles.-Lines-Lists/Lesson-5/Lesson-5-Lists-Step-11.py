# Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
# Если на вход пришло только одно число, надо вывести его же.
# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
#
# Sample Input 1:
# 1 3 5 6 10
#
# Sample Output 1:
# 13 6 9 15 7
#
# Sample Input 2:
# 10
#
# Sample Output 2:
# 10


a = [int(i) for i in input().split()]
summary = 0
a_len = len(a)
sum_output = []
sum_output_string = ''
sum_str = ''
for i in range(0, a_len):
    if a_len == 1:
        print(a[0])
    else:
        if i == 0:
            summary = a[-1] + a[1]
            sum_str = str(summary)
            sum_output.append(sum_str)
        elif i < a_len - 1:
            summary = a[i - 1] + a[i + 1]
            sum_str = str(summary)
            sum_output.append(sum_str)
        else:
            summary = a[a_len - 2] + a[0]
            sum_str = str(summary)
            sum_output.append(sum_str)
sum_output_string = ' '.join(sum_output)
print(sum_output_string)
