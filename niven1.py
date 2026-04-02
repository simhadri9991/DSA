def is_niven(n):
    temp=n
    digit_sum=0
    while temp>0:
        digit=temp%10      
        digit_sum+=digit   
        temp//=10            
    if n%digit_sum==0:
        return True
    else:
        return False
num=156
if is_niven(num):
    print("it is a Niven Number",num)
else:
    print("It is NOT a Niven Number",num)