#Q27 — First Repeated Word

#Write a Python program to find the first 
#word that appears more than once in a sentence.
s=input("enter the string:")
current_word=""
printed=""
found=False
for i in s:
    #current_word=""
    if i==" ":
        
        if current_word  in printed:
            print(current_word)
            found=True
            break
            
        else:
            printed=printed+" "+ current_word
        current_word=""
            
    else:
        current_word=current_word+i
# Process the last word
if not found and current_word != "":
    if current_word in printed:
        print("First repeated word:", current_word)
        found = True

if not found:
    print("No repeated word")


    
