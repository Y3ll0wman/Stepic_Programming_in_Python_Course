# Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
#
# Для решения задачи может пригодиться метод sort списка.
#
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
#
# Sample Input 1:
# 4 8 0 3 4 2 0 3
#
# Sample Output 1:
# 0 3 4
#
# Sample Input 2:
# 10
#
# Sample Output 2:
#
# Sample Input 3:
# 1 1 2 2 3 3
#
# Sample Output 3:
# 1 2 3
#
# Sample Input 4:
# 1 1 1 1 1 2 2 2
#
# Sample Output 4:
# 1 2


a = [str(i) for i in input().split()]
a_sort = sorted(a)
a_double = []
a_len = len(a_sort)
a_str = ''
a_output_string = ''
for i in range(0, a_len - 1):
    if a_sort[i] == a_sort[i + 1]:
        if a_sort[i] in a_double:
            continue
        else:
            a_str = str(a_sort[i + 1])
            a_double.append(a_str)
a_output_string = ' '.join(a_double)
print(a_output_string)
