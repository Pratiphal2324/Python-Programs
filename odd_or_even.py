num: int = input("Enter a number: ")
if int(num) == 0:
    print(num + " is neither odd nor even.")
elif int(num) % 2 == 0:
    print(num + " is an even number.")
else:
    print(num + " is an odd nnumber.")


# Alternative approach - Short hand if else
print(f"{num} is neither odd nor even" if int(num) == 0 else f"{num} is even" if int(num) % 2 == 0 else f"{num} is odd")