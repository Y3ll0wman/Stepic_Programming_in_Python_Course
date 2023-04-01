# Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
# Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
#
# Попробуем написать подобную систему.
#
# На вход программе первой строкой передаётся количество d известных нам слов, после чего на d строках указываются эти слова. Затем передаётся количество l строк текста для проверки, после чего l строк текста.
#
# Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
#
# Sample Input:
# 4
# champions
# we
# are
# Stepik
# 3
# We are the champignons
# We Are The Champions
# Stepic
#
# Sample Output:
# stepic
# champignons
# the


d = int(input())
words = set()
unknow_words = set()

for _ in range(d):
    words.add(input().lower())

l = int(input())


for _ in range(l):
    string = input().lower().split()

    for i in range(len(string)):
        if string[i] not in words:
            unknow_words.add(string[i])

for word in unknow_words:
    print(word)
