#Find the length of a string without using len()
s=input("string:")
count=0
for ch in s:
    if ch in s:
        count=count+1
print("Count:",count)
