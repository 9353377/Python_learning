#Write a Python program to print all characters 
#that appear more than once, without using set(),

s=input("enter the string: ")
charcters=""
for i in range(1,len(s)):
    if s[i]==s[i-1]:
          print(s[i-1])