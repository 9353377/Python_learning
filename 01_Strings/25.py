#Anagram
s1=input("enter 1st string:")
s2=input("enter 2nd string:")
if len(s1)!=len(s2):
    print("not anagram")
    
else:
    is_anagram=True
    for i in s1:
        count1=0
        for ch in s1:
            if ch==i:
                count1 += 1
        count2=0
        for ch in s2:
            if ch==i:
                count2 += 1
        if count1!=count2:
            is_anagram=False
            break
    if is_anagram:
        print("They are anagram")
    else:
        print("not anagram")

    
