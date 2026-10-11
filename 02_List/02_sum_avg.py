"""Write a program that:

Takes 5 numbers from the user.
Stores them in a list.
Finds the sum without using sum().
Finds the average.
Prints both."""

numbers=[]
for i in range(5):
    n=int((input("enter the numbers: ")))
    numbers.append(n)
total=0
for i in range(len(numbers)):
    total=total + numbers[i]
avg=total/len(numbers)
print("Sum=",total)
print("Average=",avg)

        
 