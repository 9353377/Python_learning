#Write a Python program to check whether two strings are rotations of each other
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Not Rotation")
else:
    is_found = False

    for i in range(len(s1)):
        result = ""

        for ch in range(1, len(s1)):
            result = result + s1[ch]

        result = result + s1[0]

        s1 = result

        if s1 == s2:
            is_found = True
            break

    if is_found:
        print("String Rotation")
    else:
        print("Not Rotation")