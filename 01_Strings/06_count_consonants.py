#count the number of consonants in string
s=input("enter string:").lower()
count=0
for i in s:
    if i not in "aeiou" and "0 "<= i <= "9":
        count=count+1
print(count)