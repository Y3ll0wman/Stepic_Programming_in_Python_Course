# Коля каждый день ложится спать ровно в полночь и недавно узнал, что оптимальное время для его сна составляет X минут. Коля хочет поставить себе будильник так, чтобы он прозвенел ровно через X минут после полуночи, однако для этого необходимо указать время сигнала в формате часы, минуты. Помогите Коле определить, на какое время завести будильник.
#
# Часы и минуты в выводе программы должны располагаться на разных строках (см. пример работы программы)
#
# Помните, что для считывания данных нужно вызывать функцию input без аргументов!


x = input()
print(int(x) // 60)
print (int(x) % 60)
