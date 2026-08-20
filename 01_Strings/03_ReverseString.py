"""s=input("Enter string:")
reversed=" "
for ch in s:
    reversed=ch+reversed
print(reversed)"""

""" #by using reversed keyword
s=input("string")
reversed_text=""
for ch in reversed(s):
    reversed_text=reversed_text+ch
print(reversed_text)"""
    

s=input("string")
reversed_text=s[: : -1]
print(reversed_text)

