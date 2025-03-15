set1 = set()
set2 = set()
print("For first set: ")
while True:
    inp = input("Enter element('exit' to exit): ")
    if str.lower(inp) == "exit":
        break
    set1.add(int(inp))
# print(set1)
print("For second set: ")
while True:
    i = input("Enter element('exit' to exit): ")
    if str.lower(i) == "exit":
        break
    set2.add(int(i))
# print(set2)
print(set1.union(set2))
