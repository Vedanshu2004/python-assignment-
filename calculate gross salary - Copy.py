BS = float(input('enter the basic sallary : '))
if( BS <= 10000):
    HRA = .20* BS
    DA = .80*BS
    GS = BS + HRA + DA
    print('Gross salary of employee is : ',GS)
elif( BS > 10000 and BS <=20000):
    HRA = .25*BS
    DA = .90*BS
    GS = BS + HRA + DA
    print('Gross sallary of employee is : ',GS)
else:
    HRA = .30*BS
    DA = .95*BS
    GS = BS + HRA + DA
    print('Gross salary of employee is : ',GS)
