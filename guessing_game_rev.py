import random

tries = 0
minimum = 0
maximum = 500
playing = True
while playing == True:
    rNum = random.randint(minimum, maximum)
    res = input("\nIs it " + str(rNum) + "? ")
    if "yes" in res.lower():
        print("\nIt took " + str(tries) + " tries.")
        playing = False
    elif "no" in res.lower() and " lower" in res.lower():
        maximum = rNum
        tries += 1
    elif "no" in res.lower() and " higher" in res.lower():
        minimum = rNum
        tries += 1
    else:
        break
