# считать 2 числа с консоли.Вывести наиюольшее из этих чисел.
number1 = int(input('Введите первое число:'))
number2 = int(input('Введите второе число:'))
if number1 > number2:
	print(str(number1),  'Наибольшее число')
elif number2 > number1:
	print(str(number2), 'Наибольлшее число!')
else:
	print('Введенные Вами значения равны.')