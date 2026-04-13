#Subarray sum
'''
arr=list(map(int,input().split()))        
maxsum=0
curr=arr[0]
for i in range(1,len(arr)):
    curr=max(maxsum,curr+arr[i])
    maxsum=max(maxsum,curr)
print("Max sum is :",maxsum)    
'''
arr=[1,2,3,-1,-2,-3,0,4]
sum1=0
for i in arr:
    if i>0:
        sum1+=i
print(sum1)        
'''
DRY RUN

'''