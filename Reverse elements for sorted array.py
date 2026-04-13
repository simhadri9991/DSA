#Reverse elements for array (sorted and unsorted)
'''
arr=list(map(int,input().split()))
start=0
end=len(arr)-1
while start<end:
    arr[start],arr[end]=arr[end],arr[start]
    start+=1
    end-=1
print(arr)    
'''
