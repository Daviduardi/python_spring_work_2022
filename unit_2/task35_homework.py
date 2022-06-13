# todo: Реализовать полный функционал системы. Любой класс можно расширить до той функциональности которая
# потребуется в результате написания кода.



# НЕ ПОНИМАЮ ДАЛЬШЕ КАКИЕ И КАК КЛАССЫ ОПИСЫВАТЬ. ПОЭТОМУ НЕ МОГУ ПРИСТУПИТЬ К 36 ЗАДАНИЮ И ЗАКОНЧИТЬ РАБОТУ

import psycopg2
import bcrypt

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
        cur.execute(f"""SELECT "password" FROM "student" WHERE "login" = '{login}'""")
        obj = cur.fetchall()
        return obj


class Auth:
    """Класс содержит методы регистрации, захода в систему и выхода из нее"""
    def __init__(self):
        self.conn = DB("testsystem", "testsystem", "123").get_connect()


    def login(self, login = None, password = None):
        """Метод аутентификации пользователя в системе"""
        self.login = str(input("Enter login: "))
        self.password = str(input("Enter password: "))
        self.user = DB("testsystem", "testsystem", "123").get_profile(self.conn, self.login)
        if self.user:
            if self.password == self.user[0][0]:
                self.is_auth = True
                print("Добро пожаловать!")
                Test(self.conn).get_test()
            else:
                print("Неверные password")
        else:
            Auth().registration()

    def registration(self):

        """Метод создания профиля пользователя в системе """
        print("Зарегестрируйтесь пожалуйста!")
        id_student = int(input("Введите номер группы: "))
        lastname = str(input("Введите свое фамилию: "))
        name = str(input("Введите своё имя: "))
        age = int(input("Введите свой возраст: "))
        new_login = str(input("Введите логин: "))
        new_password = str(input("Введите пароль: "))
        group = int(input("Введите номер группы: "))
        hashandsalt = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
        hashandsalt = hashandsalt.decode('utf-8')
        new_student = Profile(id_student, lastname, name, age, new_login, hashandsalt, group)
        new_student.set_profile(self.conn)

        print("Вы зарегестрированы!")
        Auth.is_auth = True


    def logout(self):
        Auth.is_auth = False


class Profile:
    def __init__(self, id_student, lastname, name, age, login, password, group):
        self.id_student = id_student
        self.lastname = lastname
        self.name = name
        self.age = age
        self.login = login
        self.password = password
        self.group = group


    def set_profile(self, conn):
        cur = conn.cursor()
        cur.execute(f'''INSERT INTO Student("id_student", "lastname", "name", "age", "login", "password", 
        "group") VALUES ('{self.id_student}', '{self.lastname}', '{self.name}', '{self.age}', '{self.login}', 
        '{self.password}', '{self.group}')''')
        conn.commit()

    def get_profile(self, conn):
        # Извлекает профиль из БД
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM Student WHERE login = '{self.login}'""")
        obj = cur.fetchall()
        conn.commit()
        return obj

# class Result:
#     def set_profile(self, conn):
#         cur = conn.cursor()
#         cur.execute(f'''INSERT INTO result("id_question", "id_test", "tm_result", "status", "answer", "id_student")
#         VALUES ({self.id_question}, {self.id_test}, {self.tm_result}, {self.status}, {self.answer}, {self.id_student}''')

# class Login(View):
#     def render(self):
#         a = "Введите логин: "
#         b = "Введите пароль: "
#         return [a, b]


class Test:
    """ В классе реализуем методы работы с БД """
    def __init__(self, connect):
        # self.dbname = dbname
        self.connect = connect

    def get_test(self):
        """В методе  получаем список тестов по темам """
        cur = self.connect.cursor()
        cur.execute("""SELECT "id_test", "theme" FROM "test" """)
        tests = cur.fetchall()
        return tests

    def get_questions(self, id_test):
        """В методе  получаем список вопросов-ответов по id теста """
        cur = self.connect.cursor()
        cur.execute(f""" SELECT "id_question", "id_answer", "num_answer" FROM "question" 
        WHERE "id_test" = {id_test} """)
        test = cur.fetchall
        return test


class TestSystem:
    "Класс взаимодействует с моделью и представлением. Включает всю бизнес логику системы."
    def run(self):
        """Метод реализует запуск теста"""
        pass

    def show_list(self):
        """Метод реализует вывод списка тестов на экран"""
        pass

    def show_question(self, id_question):
        """Метод реализует вывод списка тестов на экран"""


    def YouMethods(self):
        """Методы которые вам дополнительно понадобятся"""
#
#
# class View:
#     """ 'Абстрактный' класс для потомков """
#     def render(self):
#         pass
#
#
# class TestView(View):
#     """В классе перегружаем виртуальный метод  render от родителя"""
#
#     def render(self, data):
#         """Метод реализует отрисовку экранной формы выбора билета """
#
#
# class QuestionView(View):
#     """В классе перегружаем виртуальный метод  render от родителя"""
#
#     def render(self, data):
#         """Метод реализует отрисовку вопроса с вариантами ответа и строкой выбора варианта"""
#
#
# class RegistrationView(View):
#     """В классе перегружаем виртуальный метод  render от родителя"""
#
#     def render(self, data):
#         """Метод реализует отрисовку регистрации пользователя"""
#
#
# class LoginView(View):
#     """В классе перегружаем виртуальный метод  render от родителя"""
#
#     def render(self, data):
#         """Метод реализует отрисовку входа по логину и паролю для зарегистрированного пользователя"""




Auth().login()
#auth_user = Auth()

#auth_user.login()

# connection = DB("testsystem", "testsystem", 123)
# conn = connection.get_connect()
# aa = TestSystem(connection.conn)