import random

n1=random.randint(0,9)
n2=random.randint(0,9)


answer=str(n1)+str(n2)
print("Welcome to Cows and Bulls!")
x=input("Please enter a 2 digit number\n")
x_list = [int(digit) for digit in str(x)] 

global c
c=0
global b 
b=0

global checklist 
checklist = []

while x != answer:
    c=0
    b=0
    if x_list[0]==n1:
        c=c+1
    if x_list[1]==n2:
        c=c+1
    for digit in x_list:
        if digit == n1 or digit ==n2:
            if digit not in checklist:
                b=b+1 
        checklist.append(digit)
    print("You have"+str(c)+"cows")
    print("You have"+str(b)+"bulls")
    x=input("Try again\n")
    x_list = [int(digit) for digit in str(x)] 
    
    
if x==answer:
    print("congrats! you guessed the right number")






