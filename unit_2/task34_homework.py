#todo: Реализовать классы DB и Profile



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
        cur.execute(f"""SELECT * from "Group" where login = '{login}';""")
        obj = cur.fetchall()
        return obj

class Profile:
    def __init__(self, id_group, surname, name, patronymic, age, login, password, group_name):
        self.id_group = id_group
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age
        self.login = login
        self.password = password
        self.group_name = group_name

    def set_profile(self, conn):
        cur = conn.cursor()
        cur.execute(f'''INSERT INTO "Group"("id_user", "name", "surname", "patronymic", "age", "login",  
        "password", "group_name") VALUES ({self.id_group}, '{self.name}', '{self.surname}', '{self.patronymic}', {self.age}, 
        '{self.login}', '{self.password}', '{self.group_name}')''')
        conn.commit()


connection = DB("testsystem", "testsystem", "123").get_connect()
conn = DB("testsystem", "testsystem", "123").get_connect()

new_student = Profile(3, 'Karo', 'Stepanyan', 'Borisovich', 60, 'Karo', '12345', '1').set_profile(conn)