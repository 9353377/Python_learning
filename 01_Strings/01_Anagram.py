s1=input("enter the string:")
s2=input("enter the string:")
s1_count=0
S2_count=0
for i in s1:
    s1_count=s1_count+1                        #if len(s1) != len(s2):
for j in s2:
    S2_count=S2_count+1
if s1_count!=S2_count:
    print("not anagram")
else:
    is_anagram=True
    for i in s1:
        count1=0
        for ch in s1:
            if ch==i:
                count1=count1+1
        count2=0
        for ch in s2:
            if ch==i:
                count2=count2+1
    
        if count1!=count2:
            is_anagram=False
            break
    if is_anagram:
        print("Anagram")
    else:
        print("Not Anagram")
        

        
    """
s="banana"
count=0
for i in s:
    if i=="a":
        count=count+1
print(count)"""

