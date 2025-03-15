n = 0
list = []
while 1:
    num = int(input("Enter the number of elements: "))
    if num == 0:
        break
    for x in range(num):
        element = int(input("Enter the element no. " + str(x + 1) + ": "))
        list.append(element)
    # rankorder = sorted(range(len(thelist)), key=thelist.__getitem__)
    rankorderoflist = [sorted(list).index(x) for x in list]
    rankorder_weird = [(num - x) for x in rankorderoflist]
    print(rankorder_weird)
