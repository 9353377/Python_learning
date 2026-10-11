"""Q3 — Count Even and Odd Numbers

Take 10 numbers from the user and store them in a list.

Then:

Count how many are even
Count how many are odd
Print both counts"""

numbers=[]
for i in range(10):
    n=int(input("enter the numbes :"))
    numbers.append(n)
count1=0
count2=0
for i in numbers:
    if i%2==0:
        count1 +=1
    else:
        count2+=1
print("Count of Even Numbers:",count1)
print("Count of Odd Numbers:",count2)