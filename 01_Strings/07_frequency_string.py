#Count the frequency of each character in a string (without using dictionaries)
s = input("Enter the string: ")

printed = ""

for i in s:
    if i not in printed:
        count = 0

        for ch in s:
            if ch == i:
                count += 1

        print(i, count)

        printed = printed + i       #its not the best soln in python using dict we can findout the best soln
