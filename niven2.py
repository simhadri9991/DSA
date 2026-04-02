def is_niven(n):
    original=n       
    digit_sum=0
    while n>0:
        digit=n%10        
        digit_sum+=digit
        n//=10
    if original%digit_sum==0:   
        print("It is a Niven Number",original)    
    else:
        print("It is NOT a Niven Number",original)
is_niven(156)