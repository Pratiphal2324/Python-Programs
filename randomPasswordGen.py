import random
class Rand:
    sLetters = set(chr(x) for x in range(97, 123))
    cLetters = set(chr(x) for x in range(65, 91))
    symbols = set(["!", "#", "@", "$", "&", "*", "_"])
    numbers = set(x for x in range(0, 10))
    pas = set().union(sLetters,cLetters,symbols,numbers)
    stringify=list(str(x) for x in pas)

a = Rand()
char = a.stringify
while True:
    password: str="".join(random.choices(population=char,k=16))
    print(password)
    repeat = input("\nDo you want another one?(Y/N) : ").lower()
    # changed if else to match case for error debugging
    match repeat:
        case "y":
            continue
        case "n":
            break
        case _:
            print("Invalid Input! Please try again!")
            break
