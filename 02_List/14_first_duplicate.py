"""Q14 — Find the First Duplicate Number

Take 10 numbers from the user and store them in a list.

Find and print the first number that appears more than once"""
num=[]
for i in range(10):
    n=int(input("enter the number: "))
    num.append(n)
printed=[]
for nu in num:
    if nu in printed:
        print("first occurance:",nu)
        break
    else:
        printed.append(nu)