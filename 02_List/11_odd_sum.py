"""Q11 — Find the Sum of Odd Numbers

Take 10 numbers from the user and store them in a list.

Then find and print the sum of only the odd numbers."""
num=[]
for i in range(10):
    n=int(input("enter the number:"))
    num.append(n)
odd_sum=0
for nu in num:
    if nu%2==1:
        odd_sum +=nu
print(odd_sum)