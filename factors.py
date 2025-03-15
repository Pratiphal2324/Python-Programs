factors = []
num = int(input("Enter a number: "))
print("The factors of " + str(num) + " are: ")
for x in range(1, num):
    if num % x == 0:
        factors.append(x)
print(factors)
