#Rotate an array right by 1
'''
arr=list(map(int,input().split()))
last=arr[-1]
for i in range(len(arr)-1,0,-1):
    arr[i]=arr[i-1]
arr[0]=last
print(arr)
'''
'''
#DRY RUN
arr=[1,2,3,4,5]
last=arr[-1]-->5
i=4
for 4 in range(5-1,0,-1):
    arr[4]=arr[3] #1 2 3 4 4
    
i=3
for 3 in range(5-1,0,-1):
    arr[3]=arr[2] #1 2 3 3 4

i=2
for 2 in range(5-1,0,-1):
    arr[2]=arr[1] #1 2 2 3 4

i=1
for 1 in range(5-1,0,-1):
    arr[1]=arr[0] #1 1 2 3 4
    
arr[0]=last # 5 1 2 3 4
'''    