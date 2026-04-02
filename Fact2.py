num=int(input("Enter a number:"))
temp=num
sum=0
while temp>0:
    r=temp%10
    fact=1
    i=1
    while i<=r:
        fact*=i
        i+=1
    sum+=fact
    temp//=10
if sum==num:
    print("Strong number:",num)
else:
    print("Not a strong number:",num)
    
