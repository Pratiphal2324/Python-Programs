import random


def separate(num):
    arr = []
    while num != 0:
        rem = int(num % 10)
        arr.append(rem)
        num = int(num / 10)
    return arr


def cowbulls(num, rNum):
    cows = 0
    bulls = 0
    r_arr = separate(rNum)
    n_arr = separate(num)
    for item in r_arr:
        for x in n_arr:
            if x == item:
                bulls = bulls + 1
    for x in range(0, 4):
        if n_arr[x] == r_arr[x]:
            cows = cows + 1
    print("Cows: " + str(cows) + ", Bulls: " + str(bulls - cows))


rNum = random.randint(1000, 10000)
print("\nWelcome to the Cows and Bulls Game!\n")
guesses = 1
while True:
    inp = int(input("Enter a 4-digit number: "))
    if inp / 1000 < 1:
        print("Invalid input! Please try again.")
        break
    if inp == rNum:
        print("Congratulations! You guessed the correct number🏆")
        print("No. of Guesses: " + str(guesses))
        break
    else:
        cowbulls(inp, rNum)
        guesses = guesses + 1
        print(separate(inp))
        print(separate(rNum))
