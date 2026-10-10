"""List Basics

Write a program that:

Ask the user for 5 numbers.
Store them in a list.
Print the list.
Find the largest number without using max().
Find the smallest number without using min()."""


list=[]
for i in range(5):
    n=int(input("enter the number:"))
    list.append(n)
print(list)

largest=list[0]
for i in range(1,len(list)):
    if largest<list[i]:
        largest=list[i]
print("The largest=",largest)

smallest = list[0]

for i in range(1, len(list)):
    if smallest>list[i]:
        smallest=list[i]
print("the smallest=",smallest)