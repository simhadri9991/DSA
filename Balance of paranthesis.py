#Balanced of the parathesis
s= input("enter Expression :")
stack=[]
result=""
for ch in s:
    if ch=='(':
        stack.append(ch)
        result+=ch
    elif ch==')':
        if len(stack)>0:
            stack.pop()
            result+=ch
        else:
            result='('+result+')'
while len(stack)>0 :
    result+=')'
    stack.pop()
print("balanced :",result)