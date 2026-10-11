"""Q4 — Find the Second Largest Number

Take 10 numbers from the user and store them in a list.

Find and print the second largest number."""
numbers = []

for i in range(10):
    n = int(input("Enter the number: "))
    numbers.append(n)

largest = numbers[0]
second_largest = numbers[0]

for i in range(1, len(numbers)):

    if numbers[i] > largest:
        second_largest = largest
        largest = numbers[i]

    elif numbers[i] > second_largest:
        second_largest = numbers[i]

print("Second largest =", second_largest)
            

