#Является ли год високосным. Если да то вывести текст 'високосный'. Есди нет то вывести текст обычный
year = int(input('Введите год:'))
if year % 4  == 0 and year % 100 != 0 or year % 400 == 0:
	print('Это високоный год.')
else:
	print('Это обычный год.')