#Q29 — Find All Anagrams in a String
#This will introduce a useful new pattern, 
#but we'll build it step-by-step rather than throwing the full problem at you.
s = input("Enter the main string: ")
target = input("Enter the target string: ")

found = False

for i in range(len(s) - len(target) + 1):

    substring = ""

    for j in range(i, i + len(target)):
        substring = substring + s[j]

    # Check if substring is an anagram of target
    if len(substring) == len(target):

        is_anagram = True

        for ch in target:
            count1 = 0
            count2 = 0

            for x in target:
                if x == ch:
                    count1 += 1

            for x in substring:
                if x == ch:
                    count2 += 1

            if count1 != count2:
                is_anagram = False
                break

        if is_anagram:
            print(i)
            found = True

if not found:
    print("No anagrams")