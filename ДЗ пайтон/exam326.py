#----------------------------Задача------------------------------------#
# Напишите функцию, которая будет принимать,
# числа (могут быть разного кол-во) и находить среднее
# арифметическое для данного набора


try:
    start = int(input("start =  "))
    end = int(input("end = "))
    if start > end:
        start, end = end, start
except: #ValueError or TypeError:
    raise "указан неверный тип данных"
summ = 0
for num in range(start, end+1):
    print(summ, "+", num, "=", summ + num)
    summ += num
    count = end - start + 1
    print(f"{summ} / {count} = {summ/count}")