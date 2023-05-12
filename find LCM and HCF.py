number1 = int(input('enter the numebr1 :'))
number2 = int(input('enter the number2 :'))
if(number1 >number2):
    small = number2
else :
    small = number1
for i in range(1,small+1,1):
    if(((number1%i) == 0) and ((number2%i) == 0)):
        GCD = i
print('HCF is ', GCD)
LCM = number1*number2 //GCD
print('LCM is ',LCM)
