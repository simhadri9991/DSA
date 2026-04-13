'''Find the minimum value'''
arr=list(map(int, input("Enter the numbers:").split()))
minvalue=arr[0]
for i in arr:
    if i<minvalue:
        minvalue=i
print(minvalue)

#----- Dry Run ----
'''
arr=[11,12,13,14]
len(arr)=4
for 0 -> 3
arr[0]+1 = 11+1 = 12
arr[1]+1 = 12+1 = 13
arr[2]+1 = 13+1 = 14
arr[3]+1 = 14+1 = 15

2 1 3 4

m=2
for 0 -> 3
if 2<2 F
for 1<2 T

m=1

for 3<1: F
for 4<1: F
min=1
'''
