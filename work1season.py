a = int(input('Введите число месяца (от 1 до 12):'))
if a > 0 and a <= 2 or a == 12:
	print("Время года - Зима.")
elif a > 0 and a >= 3 and a <= 5:
	print('Время года - Весна.')
elif a > 0 and a >= 6 and a <= 8:
	print('Время года - Лето.')
elif a > 0 and a >= 9 and a <= 11:
	print('Время года - Осень')
else:
	print('Ошибка. С таким числом месяца не существует!')
	print('Попробуйте снова.')