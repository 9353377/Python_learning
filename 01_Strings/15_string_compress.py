#Write a Python program to compress a string by counting consecutive repeated characters
s = input("Enter string: ")

if not s:
    print("")
else:
    count = 1
    compressed = ""

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1] + str(count)
            count = 1

    # Add the final character group
    compressed += s[-1] + str(count)

    print(compressed)