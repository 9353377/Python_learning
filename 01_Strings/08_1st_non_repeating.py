#Write a Python program to print the first non-repeating character in a string
s=input("enter string:")
is_found=False
for i in s:
    count=0
    for ch in s:
        if ch==i:
            count+=1
    
    if count==1:
        is_found=True
        print(i)
        break
if not is_found:
    print("no non-repesting characters exit")
     