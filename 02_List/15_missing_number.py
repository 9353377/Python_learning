"""Q15
Find the missing number

Take 9 different numbers from 1 to 10 and store them in a list. Exactly one number will be missing."""

E = [1,2,3,4,5,6,7,8,9,10]

u = []

for i in range(9):
    n = int(input("Enter the number: "))
    u.append(n)

for i in E:
    found = False

    for nu in u:
        if i == nu:
            found = True
            break

    if found == False:
        print("Missing number:", i)
        break


