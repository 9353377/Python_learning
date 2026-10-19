"""Q13 — Count Frequency of a Target
Take 10 numbers and store them in a list.
Then take a target number from the user.
Find and print how many times the target appears in the list."""

num=[]
for i in range(10):
    n=int(input("enter the number: "))
    num.append(n)
tar=int(input("enter the target: "))
count=0
for nu in range(0,len(num)):
    if tar==num[nu]:
        count+=1
print("Frquency is:",count)