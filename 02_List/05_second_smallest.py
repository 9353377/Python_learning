"""Q5 — Find the Second Smallest Number
Take 10 numbers from the user and store them in a list.
Find and print the second smallest number."""

Numbers=[]

for i in range(5):
    n=int(input("Enter the Number: "))
    Numbers.append(n)
smallest=Numbers[0]
second_smallest=None

for i in range(1,len(Numbers)):
    if Numbers[i]<smallest:
        second_smallest=smallest
        smallest=Numbers[i]

    elif Numbers[i] != smallest:
        if second_smallest is None or Numbers[i] < second_smallest:
            second_smallest=Numbers[i]

print("The Second Smallest Number is:",second_smallest)