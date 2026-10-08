#Q28 — Longest Palindromic Substring

#Given a string, find the longest substring that is a palindrome.

s=input("enter the string:")
longest_palindrome=""
for i in range(len(s)):
    substring=""
    for j in range(i,len(s)):
        substring=substring+s[j]
        reverse = ""

        for k in range(len(substring)-1, -1, -1):
            reverse = reverse + substring[k]
        
        if substring == reverse:
            
            if len(substring)>len(longest_palindrome):
                longest_palindrome=substring

print("Palindrome:", longest_palindrome)
        