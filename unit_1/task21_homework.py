# todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html


page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}

#template = """
#<!DOCTYPE HTML>
#<html>
# <head>
#  <title> ? </title>
#  <meta charset=?>
# </head>
# <body onload="alert(?)">
#  <p>?</p>
# </body>
#</html>
#"""

f = open("index.html", "r", encoding="utf-8")

list_ = f.readlines()
f.close()

list_[4] = str(list_[4])[:9] + page["title"] + str(list_[4])[11:]
list_[5] = str(list_[5])[:16] + page["charset"] + str(list_[5])[17:]
list_[7] = str(list_[7])[:21] + page["alert"] + str(list_[7])[22:]
list_[8] = str(list_[8])[:5] + page["p"] + str(list_[8])[6:]

print(list_)

f_new = open("index.html", "at+", encoding="utf-8")
for element in list_:
        f_new.write(element)

f_new.close()

