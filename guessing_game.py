def printScores(score, hScore):
    print("\nScore : " + str(score))
    print("High Score : " + str(hScore))


import random

rNum = random.randint(1, 19)
hScore = 0
score = 15
while True:
    inp = int(input("\nGuess a number between 0 and 20!🤔: \n"))
    if inp == rNum:
        print("\nCongratulations! You guessed the right number🏆\n")
        if score > hScore:
            hScore = score
        printScores(score, hScore)
        repeat = input("\nDo you want to play again?(Y/N) : ")
        if str.lower(repeat) == "y":
            rNum = random.randint(1, 19)
            score = 15
            continue
        elif str.lower(repeat) == "n":
            break
        else:
            print("Invalid Input! Please try again!")
            break
    else:
        print("\nYou're Wrong!❌\n")
        score = score - 1
        printScores(score, hScore)
        if score > 0:
            continue
    if score == 0:
        print("\nYou Lose!😢\n")
    rep = input("\nDo you want to play again?(Y/N) : ")
    if str.lower(rep) == "y":
        rNum = random.randint(1, 19)
        score = 15
        continue
    elif str.lower(rep) == "n":
        break
    else:
        print("Invalid Input! Please try again!")
        break
