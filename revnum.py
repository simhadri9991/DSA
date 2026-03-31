''' Write a code to add the sum of digits of a given number'''
n=int(input("Enter a number:"))
s=0
while n!=0:
    r=n%10
    print(r, end="")
    n=n//10