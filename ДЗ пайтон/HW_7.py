#------------------------задача---------------------------#
# Вывести на экран фигуру из звездочек:
# *******
# *******
# *******
# *******
# (квадрат из n строк, в каждой строке n звездочек)
# n - гарантируется, что целое число


# strings = 4 # как-то получили значение
# string_1 = 7 # в первой строке кол-во звездочек 7
#
# while strings != 0:
#     strings -= 1
#     if string_1 == 7:
#         string_1 = 7
#         print("*******")
#     elif string_1 == 7:
#         string_1 = 7
#         print("*******")
#     else:
#         print("неправльное значение")


#------------------------задача---------------------------#
# распечатайте все числа, которые делятся на 3 от start до end(включительно)
# (start, end - могут быть перепутаны),
# start , end- гарантируется, что целые числа
start = 1
end = 100
if start <= end:
    for n in range(start, end+1):
        if n%3 == 0:
            print(n)
else:
    if end % 3 != 0:
        end += 1
    for n in range(end, start+1, 3):
        print(n)
