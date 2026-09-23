#Write a Python program to reverse each word individually, while keeping the word order unchanged.

s = input("Enter words: ")
current_word = ""
result = ""

if not s:
    print("empty sentence")
else:
    for ch in s:
        if ch == " ":
            if current_word != "":
                for i in range(len(current_word)-1, -1, -1):
                    result = result + current_word[i]

                result = result + " "
                current_word = ""
        else:
            current_word = current_word + ch

    # Reverse the last word
    for i in range(len(current_word)-1, -1, -1):
        result = result + current_word[i]

    print(result)