#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
#– id - номер по порядку (от 1 до 10);
#– текст из списка algoritm

#algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
#"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

#Каждое значение из списка должно находится на отдельной строке


f = open("algoritm.csv", "w", encoding="UTF8")       #Создался файл в экселе. но то что по русски написано почему то непонятными буквами в этом файле отображает

id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

new = []
for i in range(len(id)):
    f.write(str(id[i])+ "-" + str(algoritm[i]) + "\n")

f.close()