#Написать калькулятор
#+|-|/|*|mod|pow|div
#Деление на ноль - ошибка
a = float(input('Введите первое число:'))
b = float(input('Введите второе число:'))
operation = input('Что делаем (+|-|/|*|%|**|//|)?:')

if operation == '+':
	print(a + b)
elif operation == '-':
	print(a - b)
elif operation == '/':
	if b == 0:
		print('Ошибка! Деление невозможно.')
	else:
		print(a / b)
elif operation == '*':
	print(a * b)
elif operation == 'mod':
	if b == 0:
		print('Ошибка! Действие неаозможно.')
	else:
		print(a % b)
elif operation == 'pow':
	print(a ** b)
elif operation == 'div':
	if b == 0:
		print('Ошибка! Действие невозможно.')
	else:
		print(a // b)
	