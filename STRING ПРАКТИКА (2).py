#задача 1
#Пользователь вводит тип фигуры и программа считает ее площадь
type = input()
if type == "треугольник":
	a = int(input())
	b = int(input())
	c = int(input())
	p = (a + b + c) / 2
	print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif type == "прямоугольник":
	a = int(input())
	b = int(input())
	print(a * b)
elif type == 'круг':
	r = int(input())
	print(3.14 * r ** 2)
	
#задача 2
#Определить является ли введенная строка палиндромом 
#Палиндром - это строка, которая с одной и с другой стороны читается одинаково (как цифры так и буквы),(121  / aba)
#text = '121'
#text[ : : -1] (этот прием переворачивает строчку)
text = input()
a = text[ : : -1]
if a == text:
	print('Палиндром')
else:
	print('Обычная строка')

#задача 3
#Дана строка, определить колиество слов в ней (жостаточно посчитать кол-во пробелов + 1)
text = input()
n = text.count(' ') + 1
print (n)

#задача 4
#дана строка. Разрезать ее на две равные части
#поменять эти части местами
text = input()
text_1 = text[ : (len(text) + 1) // 2]
text_2 = text[(len(text) + 1) // 2 : ]
print(text_2 + text_1)

#задача 5
#Дана строка. Заменить в этой все 1(единицы) на слово one
text = input()
print(text.replace('1', 'one'))

#задача 6
#Определить четверть в которой лежит введенная точка
x = int(input())
y = int(input())
if x > 0 and y > 0:
	print('I')
elif x > 0 and y < 0:
	print('II')
elif x < 0 and y < 0:
	print('III')
elif x > 0 and y < 0:
	print('IV')