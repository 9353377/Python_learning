"""Q9 — Remove All Zeros
Take 10 numbers from the user and store them in a list.
Create a new list containing all numbers except zero."""

num=[]
for i in range(10):
    n=int(input("enter te number: "))
    num.append(n)
new_list=[]
for nu in num:
    if nu!=0:
        new_list.append(nu)

print(new_list)
