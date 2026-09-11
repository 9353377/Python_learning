s=input("Input=")
is_only_alphabat=True
for ch in s:
    if not ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
        is_only_alphabat=False
        break
if is_only_alphabat:
    print("only Alphabat")
else:
    print(" contains non-alphbatic characters also")