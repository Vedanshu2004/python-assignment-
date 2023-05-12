# Write a Python program to calculate sum of digits of a number.
n = int(input("enter the number :"))
temp = n
sum = 0
while(n > 0):
    rem = n%10
    n = n//10
    sum = sum + rem
print('sum of digit is :',sum)
