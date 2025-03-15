import random as R


class Rand:
    sLetters = [chr(x) for x in range(97, 123)]
    cLetters = [chr(x) for x in range(65, 91)]
    symbols = ["!", "#", "@", "$", "&", "*", "_"]
    numbers = [x for x in range(0, 10)]
    pas = [sLetters, cLetters, symbols, numbers]


a = Rand()
i = a.pas
while True:
    c = 1
    p = ""
    while c <= 16:
        p = p + str(R.choice(R.choice(i)))
        c = c + 1
    print("\n" + p)
    repeat = input("\nDo you want another one?(Y/N) : ")
    if str.lower(repeat) == "y":
        continue
    elif str.lower(repeat) == "n":
        break
    else:
        print("Invalid Input! Please try again!")
        break
