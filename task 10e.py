# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно 

first_num = int(input('Введите первое число:'))
second_num= int(input('Введите второе число:'))
third_num = int(input('Введите третье число:'))

if first_num < second_num:
	first_num, second_num = second_num, first_num
if first_num < third_num:
	first_num, third_num = third_num, first_num
if second_num > third_num:
	second_num, third_num = third_num, second_num
print(first_num)
print(second_num)
print(third_num)
