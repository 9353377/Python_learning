"""Q10 — Find the Sum of Even Numbers
Take 10 numbers from the user and store them in a list.
Then find and print the sum of only the even numbers."""
num=[]
for i in range(10):
    n=int(input("enter number"))
    num.append(n)
even_sum=0
for nu in num:
    if nu % 2==0:
        even_sum +=nu
print(even_sum)

