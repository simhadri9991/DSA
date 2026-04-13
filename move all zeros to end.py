#Move all zeroes to an end 
'''
arr=list(map(int,input().split()))
zero=0
for i in range(len(arr)):
    if arr[i]!=0:  # IF WE PLACE == it will be left shift
        arr[zero],arr[i]=arr[i],arr[zero]
        zero+=1
print("After moving Zeroes:",arr)        
'''

'''
DRY RUN

1.arr=[0,1,0,3,2]
zero=0

2.arr[i]=1
as 1!=0
swap 0-1 -> 1-0
zero=1

3.
arr[i]=2
0
zero=1
skip

4.arr[i]=3
3!=0
swap 0-3 --> 3-0

5.i==4
arr[i]!=0
2!=0
swap 0-2 --> 2-0

'''