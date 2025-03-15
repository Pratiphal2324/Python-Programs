def fib(n):
    if n == 1:
        print("0")
    elif n == 2:
        print("0\n1")
    else:
        a = 0
        b = 1
        c = 1
        while c <= n:
            print(a)
            print(b)
            a = a + b
            b = a + b
            c = c + 1


n = int(input("Enter the number of fibonacci numbers to be printed: "))
fib(n)
