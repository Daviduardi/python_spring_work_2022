#todo: Для игры "Отгадай число от 0 до 100" реализованной на занятии 4 homework/task3
#написать Save Game по следующему сценарию:
#В запущенной игре по нажатию клавиши S появляется вывод:
#1. Продолжить
#2. Сохранить игру

#При выборе пункта 1. игра продолжается.
#При выборе пункта 2. пользователю предлагается ввести название для
#сохранения, после чего нужно сделать сериализацию состояния игры.
#Законсервировать все объекты которые отвечают за состоянии игры в файл
#game_dump.pkl   Сериализацию и десериализацию сделать на базе библиотеки pickle.

#При старте игры пользователю должен предлагатся выбор
#1. Новая игра
#2. Восстановить игру
#При выборе 1. начинается новая игра.
#При выборе 2. пользователю выводится список всех сохраненных игр(происходит десериализация).
#Из них он выберает нужную, после чего загружается состояние игры на момент сохранения.

import pickle
import random
from serial import to_pickle
z = random.randint(0,100)
fale = 0
print(z)
save = input("Выберите цифру:\n 1. Новая игра\n "
             "2. Сохраненные игры: \n >>")
if save == "1":
    pass
if save == "2":
    sg = open("savelist.txt", mode="r") #файл с сохраненными играми
    print("Сохраненные игры\n",sg.readlines())
    sg2 = input("Введите название сохраенной игры: ")
    with open(sg2, 'rb') as f:
        save_files = pickle.load(f)
        print(save_files)
        fale = save_files[0]
        z = save_files[1]
    sg.close()
while fale < 10:
    a = input("Введите предпологаемое число: \n" "Если хотите сохранить игру введите S или s")
    print(type(a))
    if a in ['s', 'S', 'ы', 'Ы']:
        print("Игра будет сохранена")
        savename = input("введите название игры для сохранения: ")
        fx = open("savelist.txt",  mode="at", encoding="UTF-8")
        fx.write(savename +".pkl ;")
        save1 = []
        save1 = fale, z  # сохраняем количество попыток и загаданное число
        to_pickle(save1, f"{savename}.pkl", "wb")
        fx.close()
        print("Игра сохранена!")
        break
    if a.isdigit():
       a = int(a)
       if a < z:
           fale += 1
           print("Больше.", fale,"попыток из 10")
       if a > z:
           fale += 1
           print("Меньше", fale,"попыток из 10")
       if a == z:
           print("Вы угадали")
           break
       if fale == 10:
           print("Вы проиграли")
           break