#Вводится 3 числа. Если все числа больше 10,то вывести True, иначе вывести False
a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = int(input('Введите третье число:'))
if a > 10:
	if b > 10:
		if c > 10:
			print(True)
else:
	print(False)
#2 способ. в конструкции if сделать операции сравнения and
#if a > 10 and b > 10 and c > 10:
