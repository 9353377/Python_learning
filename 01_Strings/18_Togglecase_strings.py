"""Question 18/35 — Toggle Case Without Built-ins

Write a Python program to toggle the case of every alphabet"""

s=input("enter the string:")
result=""
for ch in s:
    if "A" <= ch <= "Z":
        result=result+chr(ord(ch)+32)
    elif "a" <= ch <= "z":
        result=result+chr(ord(ch)-32)
    else:
        result=result+ch
print("Toggle of string :",result)