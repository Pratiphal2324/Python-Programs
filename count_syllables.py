def count(str):
    c = 0
    for x in str:
        if x == "-":
            c = c + 1
    return c + 1


inp = input("Enter a word with syllables seperated by hyphens: ")
syllables = count(inp)
print(syllables)
