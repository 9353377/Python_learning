"""Q12 — Search for an Element
Take 10 numbers from the user and store them in a list.
Then ask the user for one target number.
Print:
"Found" if the target exists in the list
"Not Found" if it doesn't exist."""

num=[]
for i in range(10):
    n=int(input("enter numbers:"))
    num.append(n)
t=int(input("enter target:"))
for nu in range(0,len(num)):
    if t==num[nu]:
        print("Found!,its index is=",nu)
        break
    
else:
    print("Not Found")