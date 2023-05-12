Physics = int(input('enter the marks in physics : '))
Chemistry = int(input('enter the  marks in chemistry : '))
Biology = int(input('enter the marks in biology : '))
Mathematics = int(input('enter the marks in mathematics : '))
Computer = int(input('enter the marks in computer : '))
Total = Physics + Chemistry + Biology + Mathematics + Computer 
print('total marks obtain by student is ',Total)
percentage =Total/5
print('Percentage gain by student is ',percentage)
marks = percentage 
if(marks >= 90 ):
    print('A Grade student')
elif(marks >=80  and marks <90):
     print('B Grade student')
elif(marks >= 70 and marks < 80 ):
     print('C Grade student')
elif(marks >= 60 and marks < 70 ):
     print('D Grade student')
elif(marks >= 40 and marks < 60):
     print(' E Grade students')
else:
    print('Student is fail') 
