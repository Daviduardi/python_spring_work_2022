point_A = int(input("Точка_А: "))
point_B = int(input("Точка_В: "))
point_C = int(input("Точка_С: "))

lenght_AC = point_A + point_C
lenght_BC = point_B + point_C
lenght_sum = lenght_AC + lenght_BC

print("Длина отрезка АС: ", lenght_AC)
print("Длина отрезка ВС: ", lenght_BC)
print("Длина суммы отрезков: ", lenght_sum)