#writepython prgm to print first repeatng character in string
s=input("input:")
is_found=False
for i in s:
    count=0
    for ch in s:
        if ch==i:
            count+=1
    if count>1:
        is_found=True
        print(i)
        break
if not is_found:
    print("no repeating charcters exit!")