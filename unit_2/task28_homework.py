#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
#Пример:
#render, 10,  12.05.2022 12:00
#show,    5,  12.05.2022 12:02
#render, 15,  12.05.2022 12:07
#Декоратор должен применяться для различных функций с переменным числом аргументов.
#Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

from datetime import datetime
def counter(function):
    def wrapper(*args, **kwargs):
        wrapper.count += 1

        return function
    wrapper.count = 0
    return wrapper
f = open("debug.log", 'a')
@counter
def summ(x, y):

    return x + y
summ(3, 5)
summ(6, 4)
summ(4, 5)

f.write("fuction summ" + ", ")
f.write(str(summ.count) + ", ")
f.write(str(datetime.now()))
f.write('\n')
f.close()
print("fuction summ", str(summ.count), str(datetime.now()))

f = open("debug.log", 'a')
@counter
def text(z):
    return "Hello", z
time_2 = datetime.now()
text("Masha")
text("Victor")

f.write("fuction text" + ", ")
f.write(str(text.count) + ", ")
f.write(str(datetime.now()))
f.close()
print("function text", text.count, time_2 )