#todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.

#Пример:
#mass = [1,2,17,16,30,51,2,70,3,2]

#Для числа 2 индексы двух ближайших чисел: 6 и 9

#Пример:
#mass = [1,2,17,54,30,89,2,1,6,2]
#Для числа 1 индексы двух ближайших чисел: 0 и 7
#Для числа 2 индексы двух ближайших чисел: 6 и 9

#1. Беру первый элемент массива смотрю во всем массиве совпадения если совпадения не найдены то беру 2 элемент массива и ищу совпадения в итоге
#должен получится список




mass = [1,2,4,5,2,1,2]                        # индексы выдает неверные, как исправить это? что пишу не так?

start = 0
list_elm = []
number = int(input("Введите число: "))
count = mass.count(number)
if count >= 2:
    while count:
        start = mass.index(number, start, len(mass))
        list_elm.append(start)
        start += 1
        count -= 1
    print(list_elm)


start = None
min_ = 100000

for elm in list_elm:
    if start is None:
        start = elm
        continue
    if elm - start < min_:
        min_ = elm - start
        first_index = elm
        second_index = start
        start = elm

print(first_index)
print(second_index)

