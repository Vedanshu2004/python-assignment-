#Write a program to roll the dice till the 6 number is not appear. (computer vs human)

import random
user = int(input("enter the number in range of (1 to 6) : "))
possible = ["1","2","3","4","5","6"]
computer = random.choice(possible)
print(f"\n user number = {user} , computer number = {computer}.\n")
if("user" == "computer"):
    print("Both number user and computer is equal",user)
elif("user" > "computer"):
    print("User number is greater then computer number",user )
else:
    print("computer number is greater then user number",computer)
    
