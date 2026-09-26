#Write a Python program to find the longest common prefix among a group of strings.

s1=input("enter the string1: ")
s2=input("enter the string2: ")
s3=input("enter the string3: ")
long_pre=""
shortest=s1
if len(s2) < len(shortest):
    shortest=s2
if len(s2) > len(s3):
    shortest=s3
if len(s3) > len(s1):
    shortest=s1
for i in range(0,len(shortest)):
    if s1[i]== s2[i] and s2[i]== s3[i]:
        long_pre=long_pre + s1[i]
    else:
        break
print("Longest Prefix is:",long_pre)
    
