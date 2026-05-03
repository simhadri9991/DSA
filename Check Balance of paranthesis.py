#check Balance of the parenthesis
s=input("Enter an expression:")
stack=[]
valid= True
for ch in s:
    if ch in "({[":
        stack.append(ch)
    elif ch in ")}]":
        if len(stack)==0:
            valid = False
            break
        top= stack.pop()
        if (ch==')' and top!='(') or \
        (ch=='}' and top!='{') or \
        (ch==']' and top!='['):
            valid=False
            break
if len(stack)!=0:
    valid=False
if valid:
    print("Balanced.....")
else:
    print("Not Balanced")