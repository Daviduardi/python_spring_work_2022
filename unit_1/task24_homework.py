#todo: Числа в буквы

#Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#Пример.
#Input	                            Output
#8 5 12 12 15	                    hello
#8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def nums_to_text(alphabet, nums_str):
    num_list = nums_str.split(" ")
    out_text = " "
    for i in num_list:
        if i.isdigit() == True:
            if int(i) == 0:
                out_text += (" ")
            elif int(i) > 0:
                out_text += (alphabet[int(i) - 1])
            else:
                continue
        else:
            out_text += i

    return (out_text)


input_str = "8 5 12 12 15 , 0 23 15 18 12 4 !"

output_str = nums_to_text(alphabet, input_str)

print(output_str)