# todo: 7.1 Дано целое число A. Проверить истинность высказывания: «Число A является четным».
# todo: 7.2 Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
# Примечание: В задании  требуется вывести логическое значение True, если выражение
# для введеных исходных данных является истинным, и значение False в противном случае.


number = int(input("Введите число:"))
if (number % 2) == 0:
   print(str(number) + " это четное число")
else:
   print(str(number) + " это нечетное число")