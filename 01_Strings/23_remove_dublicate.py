#Write a Python program to remove duplicate 
#characters from a string, keeping only the first occurrence.

s = input("Enter the string: ")

result = ""

for i in s:
    count = 0

    for ch in s:
        if ch == i:
            count += 1

    if count > 1 and i not in result:
        result = result + i

print("Duplicate characters:", result)