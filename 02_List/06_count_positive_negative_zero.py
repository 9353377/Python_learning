"""Q6 — Count Positive, Negative and Zero

Take 10 numbers from the user and store them in a list.

Print:

Number of positive numbers
Number of negative numbers
Number of zeros """

Numbers=[]
count0=0
countP=0
countN=0
for i in range(5):
    n=int(input("Enter the number:"))
    Numbers.append(n)
for i in range(0,len(Numbers)):
    if Numbers[i]==0:
        count0=count0 + 1
    elif Numbers[i]<0:
        countN=countN + 1
    elif Numbers[i]>0:
        countP=countP + 1
print("the number of zeros are:",count0)
print("the number of positive are:",countP)
print("the number of negative are:",countN)
