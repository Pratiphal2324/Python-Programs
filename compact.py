list = []
x = 1
while True:
    ele = int(input("Enter element in no. " + str(x) + ": "))
    if ele == 0:
        break
    list.append(ele)
    x = x + 1
evenNumbers = [x for x in list if x % 2 == 0]
print(evenNumbers)
