#while(цикл) условное_выражение:
	#инструкция
choice = 'y'
while choice.lower() == 'y':
	print('Hello')
	choice = input('Введите Y чтобы продолжить работу. Чтобы выйти из программы нажмите любую другую кнопку')
print('Работа программы завершена')

#программа которая вычесляет факториал
number = int(input())
i = 1
factorial = 1
while i <= number:
	factorial *= i
	i += 1
print(factorial)

#цикл for
#for int i in range():
        #инструкции
number = int(input())
factorial = 1
for i in range(1, number + 1):
        factorial *= i
print(factorial)
#range(1,6 + 1) = range(1,7) -> [1, 2, 3, 4, 5, 6] 

#range(stop)
#range(start, stop)
#range(start, stop, step)  stop не включается в итоговую коллекцию, шаг берется из числа step
#range(5) -> [0, 1, 2, 3, 4]
#range(1, 5) -> [1, 2, 3, 4]
#range(2, 10, 2) -> [2, 4, 6, 8]
#range(5, 0, -1) -> [5, 4, 3, 2, 1]
for i in range(5):
	print(i, end =' ')  #end Означает чем заканчивать каждую задачу
#таблица умножения
for i in range(1, 10):
	for j in range(1, 10):
		print(i*j, end = '\t')
	print('\n')

#
print('Для выхода нажмите Y')
while True:
	sum = input('Введите сумму для обмена')
	if sum.lower() == 'y':
		break # позволяет остановить программу если блок выше равен True
	money = int(sum)
	if money < 0:
		print('Сумма должна быть положительной')
		continue #позволяет продолжить запускать программу далее
	cache = round(money / 75.11)
	print(cache)
print('Работа программы завершена')
