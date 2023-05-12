n= input("enter your number:-")

#By loop 

if (n.isnumeric):
    for i in range(len(n)):
        if i == 0:
            print(f" your first digit of the number is {n[0]}")
        elif i== len(n)-1:
            print(f" your last digit of the number is {n[-1]}")
else:
    print("Please enter a number and try again!")
