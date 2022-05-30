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
connect = psycopg2.connect(dbname="testsystem", user="testsystem", password="123", host="localhost", port=5432)
connect.autocommit = True


with connect.cursor() as cur:
    cur.execute(""" CREATE TABLE "Group"
       ("id_user" serial PRIMARY KEY,
        "login" varchar(100),
        "password" varchar(100),
        "name" varchar(100),
        "surname" varchar(100),
        "patronymic" varchar(100),
        "age" varchar(100),
        "group_name" varchar(100))
        """)

with connect.cursor() as cur:
    cur.execute(
        """INSERT INTO "Group"("login", "password", "name", "surname", "patronymic", "age", "group_name") 
        VALUES ('Davo', '12345', 'David', 'Stepanyan', 'Karoevich', 29, '1')""")

print("1. Вход")
print("2. Регистрация")
selection = int(input("Выберите параметр: "))
if selection == 1:
    login = str(input("Введите логин: "))
    password = str(input("Введите пароль: "))
    with connect.cursor() as cur:
        cur.execute("""SELECT * FROM "Group" WHERE (name = '{login}' AND password '{new_password}')""")
        if cur.rowcount:
            cur.execute("""SELECT name, surname FROM Group""")
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
    new_age = str(input("Укажите ваш возраст: "))
    new_group_name = str(input("Укажите номер группы: "))
    hashandsalt = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
    hashandsalt = hashandsalt.decode('utf-8')
    with connect.cursor() as cur:
        cur.execute(f"""SELECT * FROM "Group" WHERE (name = '{new_login}' AND password = '{new_password}')""")
        if cur.rowcount:
            print("Пользователь с таким именем существует")
        else:
            cur.execute(
                ("""INSERT INTO "Group"("login", "password", "name", "surname", "patronymic", "age", "group_name") VALUES (%s, %s, %s, %s, %s, %s, %s)"""),
                [new_login, new_password, new_name, new_surname, new_patronymic, new_age, new_group_name])
        print("Добро пожаловать, ", new_name, new_surname, ". Выберите номер теста: ", sep=" ")





