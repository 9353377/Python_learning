"""Q8 — Find All Odd Numbers
Take 10 numbers from the user and store them in a list.
Create a new list containing only the odd numbers"""

num = []
for i in range(10):
    n=int(input("enter the number:"))
    num.append(n)
odd_list=[]
for i in range(0,len(num)):
    if num[i]%2==1:
        odd_list.append(num[i])
print(odd_list)
