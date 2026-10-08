#Q28 — String Compression

#Write a program to compress consecutive repeated characters.
s=input("enter the string:")
compressed_string=""
count=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        compressed_string=compressed_string+s[i-1]+str(count)
        count=1
#last word
compressed_string+=s[-1]+str(count)
print(compressed_string)