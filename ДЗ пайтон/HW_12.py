# ---- ----------------- Задача------------------------------------#
# Посчитайте кол-во чисел в произвольной строке (число это набор цифр
# перед числом и после числа ставятся пробелы).
#
# s = " 1 45 7 15 6 8 12 4 3 25 "
# s = s.split(" ")
# print(s)
# counter = 0
# for number in s:
#     if number:
#         counter+=1
# print(counter)


# Дана срока в которой буква H  встречается 2 раза, удалите первое
# и последнее вхождение буквы h и все символы между ними

s = "Hello world pythonist"
s = s.replace("h", "", 1)
print(s)