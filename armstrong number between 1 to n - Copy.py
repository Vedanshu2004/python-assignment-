# Write a Python program to print all Armstrong numbers between 1 to n

n = int(input("enter the number :"))
for i in range(1,n+1):
    sum = 0
    temp = i
    pow = len(str(i))
    while(temp > 0):
        rem = temp % 10
        sum += rem**pow
        temp = temp//10
    if( i == sum):
        print(' armstrong number is :',i)

    
