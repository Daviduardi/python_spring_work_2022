
# МНЕ КАЖЕТСЯ Я ГДЕ ТО НАПУТАЛ ПОТОМУ ЧТО ВЫДАЕТ ЭТО:
# "C:\Program Files\Python310\python.exe" C:/Users/User/Desktop/python_spring_work_2022/unit_2/task34_homework.py
# Traceback (most recent call last):
#   File "C:\Users\User\Desktop\python_spring_work_2022\unit_2\task34_homework.py", line 40, in <module>
#     conn = connection.get_connect()
#   File "C:\Users\User\Desktop\python_spring_work_2022\unit_2\task34_homework.py", line 10, in get_connect
#     connect = psycopg2.connect(host="localhost", port=5432, dbname=self.name, user=self.user, password=self.password)
#   File "C:\Program Files\Python310\lib\site-packages\psycopg2\__init__.py", line 122, in connect
#     conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
# psycopg2.OperationalError


import psycopg2


class DB:
    def __init__(self, name, user, password):
        self.name = name
        self.user = user
        self.password = password

    def get_connect(self):

        connect = psycopg2.connect(host="localhost", port=5432, dbname=self.name, user=self.user, password=self.password)
        return connect

    def get_profile(self, conn, login):
        cur = conn.cursor()
        cur.execute(f"""SELECT * from student where login = '{login}';""")
        obj = cur.fetchall()
        return obj

class Profile:
    def __init__(self, id_group, surname, name, patronityc, age, login, phone, password):
        self.id_group = id_group
        self.surname = surname
        self.name = name
        self.patronityc = patronityc
        self.age = age
        self.login = login
        self.password = password

    def set_profile(self, conn):
        cur = conn.cursor()
        cur.execute(f'''INSERT INTO student("id_group", "surname", "name", "patronity", "age", "login",  
        "password") VALUES ({self.id_group}, '{self.surname}', '{self.name}', '{self.patronityc}', {self.age}, 
        '{self.login}', '{self.password}')''')
        conn.commit()


connection = DB("testsystem", "testsystem", "123").get_connect()
conn = DB("testsystem", "testsystem", "123").get_connect()

new_student = Profile(1, 'Stepanyan', 'Gevorg', 'Karoevich', 27, 'Gevo', 333444, '1234').set_profile(conn)