#Q25 — Longest Substring Without Repeating Characters

#Given a string, find the length of the longest substring that contains no repeated characters.

s=input("enter the string : ")
largest_sub=""
for i in range(len(s)):
    current_sub=""
    for j in range(i,len(s)):
        if s[j] not in current_sub:
            current_sub=current_sub+s[j]
        else:
            break
    if len(current_sub)>len(largest_sub):
        largest_sub=current_sub

print("The Largest substring :",largest_sub)