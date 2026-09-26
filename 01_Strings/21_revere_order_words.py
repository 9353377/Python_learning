#Write a Python program to reverse the order of words, but do not reverse the characters inside each word.

s=input("Input:")
current_word=""
reversed_text=""
if not s:
    print("empty")
else:
    for ch in s:
        if ch==" ":
            if current_word!="":
                reversed_text=current_word+" "+reversed_text
                
                current_word=""
            

        else:
            current_word=current_word+ch
    
    reversed_text=current_word+" "+reversed_text
    print(reversed_text)
        