def result(p1, p2):
    if p1 == p2:
        return "🤝Draw. No one"
    elif p1 == "r" and p2 == "p":
        return "🎉Player 2"
    elif p1 == "r" and p2 == "s":
        return "🎉Player 1"
    elif p1 == "p" and p2 == "r":
        return "🎉Player 1"
    elif p1 == "s" and p2 == "r":
        return "🎉Player 2"
    elif p1 == "p" and p2 == "s":
        return "🎉Player 2"
    elif p1 == "s" and p2 == "p":
        return "🎉Player 1"
    else:
        return 0


while True:
    print("For Player 1: ")
    inp_P1 = input("Enter r, p or s: ")
    print("For Player 2: ")
    inp_P2 = input("Enter r, p or s: ")
    if result(inp_P1, inp_P2) == 0:
        print("Invalid input. Please try again.")
        continue
    else:
        print(result(inp_P1, inp_P2) + " Wins!!!")
    repeat = input("Do you want to repeat? (Y/N): ")
    if str.lower(repeat) == "n":
        break
    elif str.lower(repeat) == "y":
        continue
    else:
        print("Invalid input. Please try again.")
        continue
