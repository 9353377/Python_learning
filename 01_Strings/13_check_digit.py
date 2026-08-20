#Check whether a string contains only digits
s1=input("input:")
is_only_digits=True
for i in s1:
    if not ("0" <= i <= "9"):
        is_only_digits=False
        break
        
    
if is_only_digits:
    print("only digits!")
else:
    print("contains non digit characters")
        
