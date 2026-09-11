#Find the longest word in a sentence.
s = input("Enter the sentence: ")

current_word = ""
longest_word = ""
current_length = 0
longest_length = 0

if not s:
    print("Empty sentence")
else:
    for ch in s:

        if ch == " ":
            if current_length > longest_length:
                longest_word = current_word
                longest_length = current_length

            current_word = ""
            current_length = 0

        else:
            current_word = current_word + ch
            current_length = current_length + 1

    # Check the last word
    if current_length > longest_length:
        longest_word = current_word

    print("The longest word is:", longest_word)


