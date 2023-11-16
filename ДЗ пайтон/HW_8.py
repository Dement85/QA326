#--------------------------- ЗАДАЧА --------------------------------#
import random

#Дан список элементов 1, 3, 22, 7, 12, 8, 2

#1. показать каждый элемент, последня цифра которого 2
#2. показать сумму четных

# summ = 0
# count = 0
# for element in 1, 3, 22, 7, 12, 8, 2 :
#     if element % 10 == 2:
#         print(f"{element} оканчивается 2")
#     if element % 2 == 0:
#         summ += element
#         continue
#     print(element)
# else:
#     print(f"summ = {summ}")


#---------------------------Задача-----------------------------------------#
# Игра угадай число от 1 до 100
# реализовать подсказки (число введенное больше или меньше)
# сделать проверку на ввод числа для пользователя
# (может быть абсолютно любой символ)

computer_number = random.randint(1, 5)
user_number = 0
while user_number != computer_number:
    user_number = int(input("your number: "))
    try:
        for i in user_number:
            if i.isdigit() is not True:
                raise ValueError("Можно вводить только цифры!")
    except Exception:
        print("Можно вводить только цифры!")
        user_number = True
    if user_number < computer_number:
        print("введите число больше")
    if user_number > computer_number:
            print("введите число меньше")
    if user_number == computer_number:
        print("YOU WIN !!!")
    else: print("не угадали", end='\n ---------------------\n')


