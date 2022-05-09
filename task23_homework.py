#todo: Взлом шифра
#Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
#Попробуйте все возможные сдвиги и расшифруйте фразу.


#grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

#alphabet = "abcdefghijklmnopqrstuvwxyz"

#massege = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin"

#key = int(input("введите сдвиг: "))

#encrypted = ""

#for letter in massege:

#    nam = alphabet.find(letter)

#    new_nam = nam - key

#    if letter in alphabet:

#        encrypted = encrypted + alphabet[new_nam]

#    else:

#        encrypted = encrypted + letter

#print("Ваше сообщение: ", encrypted)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
message = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin"

def break_cesar(message, alphabet):
    res = []
    for i in range(len(message)):
        res.append(alphabet)

    return "\n".join(res)
print(break_cesar(message, alphabet))