num=int(input("Enter a number:"))
fact =1
i=1
while i<num:     #1<=3 - 2<=3 - 3<=3 - 4<=3
    fact=fact*i  #fact 1*1=1, fact 1*2=2, fact=1*2*3=6
    i+=1         #i=2 , i=3, i=4
print(fact)