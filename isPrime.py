num = int(input("Enter a number: "))
c = 0
for x in range(1, num - 1):
    if num % x == 0:
        c = c + 1
if c == 1:
    print(str(num) + " is a prime number.")
else:
    print(str(num) + " is a not prime number.")
