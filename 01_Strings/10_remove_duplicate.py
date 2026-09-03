s=input("input:")

printed=""
result=""

for i in s:
    if i not in printed:
        result=result+i
        printed=printed+i
    
print(result)



        
