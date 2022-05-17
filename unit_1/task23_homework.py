#todo: Взлом шифра
#Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
#Попробуйте все возможные сдвиги и расшифруйте фразу.


#grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.


alphabet = "abcdefghijklmnopqrstuvwxyz"
massedge = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin"
key = int(input("введите сдвиг: "))
encrypted = ""
for letter in massedge:
    nam = alphabet.find(letter)
    new_nam = nam - key
    if letter in alphabet:
        encrypted = encrypted + alphabet[new_nam]
    else:
        encrypted = encrypted + letter
print("Ваше сообщение: ", encrypted)