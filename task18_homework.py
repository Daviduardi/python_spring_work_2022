#todo:Создайте программу, которая будет выводить все возможные комбинации при броске 2 игральных костей
#и сумму их значений. У игральной кости стороны пронумерованы от 1 до 6.

#Пример вывода:
#Сумма 2   комбинация [(1,1)]
#Сумма 3   комбинация [(1,2),(2,1)]
#Сумма 4   комбинация [(1,3),(3,1),(2,2)]
#........................................
#Выводы комбинаций оформить в список кортежей.



dice_1 = [1, 2, 3, 4, 5, 6]
dice_2 = [1, 2, 3, 4, 5, 6]



for summ in range(2, 13):
    list = []
    for i in dice_1:
        for j in dice_2:
            if summ == j+i:
                list.append((i, j))
    else:
        print(summ, list)