# Write a Python program to check whether a number is Perfect number or not.
n = int(input("enter the number :"))
sum = 0
temp = n
for i in range(1,n,1):
    if((n//i)== 0):
        sum = sum + i
if(sum == temp):
    print("number if perfect number")
else:
    print("number is not perfect number")
