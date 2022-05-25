# #todo: Написать авторизацию пользователя в систему.
# Приложение в начале должно предлагать меню
# 1. Вход
# 2. Регистрация
#
#
# 1. При выборе пункта "Вход" пользователю необходимо ввести
# логин и пароль, поэтапно.
# login: _________
# password: ________
# При вводе данных авторизации, система проверяет есть ли данный
# пользователь в БД (логин) если нет то предлагает зарегистрироваться.
# Если есть и пароли совпадают, то происходит вход в систему. Пользователю показывается
# приглашение вида "Добро пожаловать Вася Пупкин!" и выпадает меню
# выбора билетов для тестирования(пока заглушка).
#
# 2. При выборе "Регистрация" пользователю необходимо ввести новый
# логин, пароль, фио, почту, телефон, группу. После система заводит
# запись в БД если пользователя под данным логином нет. Если такой пользователь
# уже существует то программа выдает об этом сообщение. Пароль необходимо хранить в БД
# в виде хеша + соль.
#
# По хешированию прочитать статью
# https://pythonist.ru/heshirovanie-parolej-v-python-tutorial-po-bcrypt-s-primerami/
# # для хеширования пароля воспользоваться библиотекой bcrypt

import psycopg2
import bcrypt

#Создаем таблицу в БД и заносим туда пользователя
connect = psycopg2.connect(dbname="testsystem", user="testsystem", password="123", host="localhost", port="5432")
connect.autocommit = True


with connect.cursor() as cur:
    cur.execute(""" CREATE TABLE "test_group"
       ("id_user" serial PRIMARY KEY,
        "login" varchar(100),
        "password" varchar(100),
        "name" varchar(100),
        "surname" varchar(100),
        "patronymic" varchar(100),
        "phone_number" varchar(100),
        "group" varchar(100))
        """)

with connect.cursor() as cur:
    cur.execute(
        "INSERT INTO test_group(login, password, name, surname, patronymic, phone_number, group) "
        "VALUES ('Davo', '12345', 'David', 'Stepanyan', 'Karoevich', 444555, 'a12')")

print("1. Вход")
print("2. Регистрация")
selection = int(input("Выберите параметр: "))
if selection == 1:
    login = str(input("Введите логин: "))
    password = str(input("Введите пароль: "))
    with connect.cursor() as cur:
        cur.execute("SELECT * FROM test_group WHERE name = %s AND password %s", [login, password])
        if cur.rowcount:
            cur.execute("SELECT name, surname FROM test_group")
            name_usr = cur.fetchone()
            print("Привет, ", " ".join(name_usr), "Выберите номер теста: ")
        else:
            print("Логин и пароль не найдены, пройдите регистрацию!")

elif selection == 2:
    new_login = str(input("Придумайте логин: "))
    new_password = str(input("Придумайте пароль: "))
    new_name = str(input("Укажите Ваше имя: "))
    new_surname = str(input("Укажите Вашу фамилию: "))
    new_patronymic = str(input("Укажите Ваше отчество: "))
    new_phone_number = str(input("Укажите номер телефона: "))
    new_group = str(input("Укажите номер группы: "))
    hashandsalt = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
    hashandsalt = hashandsalt.decode('utf-8')
    with connect.cursor() as cur:
        cur.execute("SELECT * FROM test_group WHERE name = %s AND password %s", [new_login, new_password])
        if cur.rowcount:
            print("Пользователь с таким именем существует")
        else:
            cur.execute(
                "INSERT INTO test_group (login, password, name, surname, patronymic, phone_number, group) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                [new_login, new_password, new_name, new_surname, new_patronymic, new_phone_number, new_group])
        print("Добро пожаловать, ", new_login, new_surname, ". Выберите номер теста: ", sep=" ")





