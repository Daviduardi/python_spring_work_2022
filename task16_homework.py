#todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
#функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
#чтобы каждая функция выполняла одно универсальное действие.



import random
print("Привет! Давай сыграем в игру угадай слово?")

questions = ["Мозг компьютера?", "Почерк компьютера"]
answers = ["процессор", "шрифт"]

questions_numbers = random.randint(0, len(questions))         # Тут программа должна выбрать вопрос из списка

word = [letter for letter in str(answers[int(questions_numbers)])]   #создаем список букв для ответа
place = [symbol for symbol in str(" " * len(answers[int(questions_numbers)]))]  # создание место ответа
print(questions[questions_numbers])
print(place)

mistake = 0                                #счетчик ошибок
right = 0                                  #счетчик верных ответов

letter = str(input("Введите букву: "))     #вводим букву
try_number = 10                            #сколько попыток у игрока

def game(questions_numbers, answers):
    while right < len(answers[int(questions_numbers)]):  # если угадал букву
        if letter in word:
            place[int(word.index(letter))] = letter
            print(place)
            right = right + 1
            if right == len(answers[int(questions_numbers)]):  # если угадает слово сразу!
                print("Поздравляю, ты угадал! Красавчик!")
            else:  # продолжать если угадана буква или несколько букв
                letter = str(input("Вводите следующую букву: "))
                continue
        else:  # если ввел букву которой нет
            mistake = mistake + 1
            if mistake < try_number:  # если количество ошибок не превышает разрешонное(10)
                letter = str(input("Такой буквы нет. Введи новую букву: "))
                continue
            else:  # если число ошибок больше (100
                print("Ты не смог угадать!Удача придет в следующий раз!")
                break