# Выведите таблицу размеромn×n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
#
# Sample Input:
# 5
#
# Sample Output:
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9


def spiral(n):
    dx, dy = 1, 0
    x, y = 0, 0
    my_array = [[None] * n for j in range(n)]
    for i in range(1, n ** 2 + 1):
        my_array[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and my_array[nx][ny] == None:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    return my_array


def print_spiral(my_array):
    n = range(len(my_array))
    for y in n:
        for x in n:
            print(my_array[x][y], end=' ')
        print()


n = int(input())
print_spiral(spiral(n))