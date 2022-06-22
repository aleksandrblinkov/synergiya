number = 25
condition = True

while condition:
    riddle = int(input("Введите целое число:"))

    if riddle == number:
        print("Поздравляю, Вы угадали.")
        condition = False
    elif riddle < number:
        print("Нет, загаданное число немного меньше этого.")
    else:
        print("Нет, загаданное число немного больше этого.")
else:
    print("Цикл завершен.")
print("Завершение.")
