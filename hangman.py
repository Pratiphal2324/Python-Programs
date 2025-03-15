# import wonderwords
# from wonderwords import RandomWord
# r = RandomWord()
# inp = r.word(word_min_length = 5, word_max_length = 7, include_parts_of_speech=["nouns"])
inp = (input("Enter the word: ")).upper()
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
num = len(inp)
print("\nThe Game Starts!\nEnter '0' to exit\nLives left = 5\n")
c = 6
arr = []
temp = []
guessed = set(temp)
for x in range(0,num):
    arr.append("_")
while(1):
    guess = input("\nGuess a letter: ").upper()
    if(guess):
        if(guess==inp):
            print("\nCongrats!! You Won!!!\n")
            print("Score: "+str(c))
            break
        if len(guess)>1:
            print("\nInvalid input! Please try again!\n")
            continue
        if guess in guessed:
            print("\nAlready guessed "+guess+" Try again!\n")
            continue
        if guess=="0":
            break
        else:
            guessed.add(guess)
        if c==0:
            print("\nGame Over!")
            print("The word was"+inp)
            break
        if guess in inp:
            print("\nCorrect Guess!")
            print("\nLives left = "+str(c))
            for x in range(0,num):
                if(inp[x]==guess):
                    arr[x] = guess
            for i in arr:
                print(i,end=" ")
            print("\nGuessed Letters : "+','.join(guessed)+"\n")
        else:
            c=c-1
            print("\nWrong guess!")
            print("\nLives Left = "+str(c))
            for i in arr:
                print(i,end=" ")
            print("\nGuessed Letters : "+','.join(guessed)+"\n")
        if(''.join(arr)==inp):
            print("\nCongrats!! You Won!!!\n")
            print("Score: "+str(c))
            break