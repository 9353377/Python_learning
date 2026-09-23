"""Question 19/35 — Count Words Without split()

Write a Python program to count the number of words in a sentence without using split()."""


s=input("enter the sentence:")
count=0
previous=" "

if not s:
    print("enter sentence with words")
else:
    
    for w in s:
        
        if w!=" " and previous == " ":
            count=count+1
        previous=w
print(f"total words are={count}")