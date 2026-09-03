#Check whether a string is a Palindrome?
s=input("enter the string:")
original=s
reversed_text=""
for i in range(len(s)-1,-1,-1):
    reversed_text=reversed_text+s[i]
print(reversed_text)
print()
if original==reversed_text:
    print("palindrome")
else:
    print("not palindrome")