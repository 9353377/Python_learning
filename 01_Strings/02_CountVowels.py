string=input("enter the string:")
count=0
for i in string:
    if i in "aeiou":
        count=count+1
print(count)
