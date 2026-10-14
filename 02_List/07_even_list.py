"""Q7 — Find All Even Numbers
Take 10 numbers from the user and store them in a list.
Then create a new list containing only the even numbers"""
num=[]
for i in range(10):
    n=int(input("enter the numbers:"))
    num.append(n)
even_list=[]
for i in range(0,len(num)):
    if num[i]%2==0:
        even_list.append(num[i])
print(even_list)
    