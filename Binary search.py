'''
algorith:
1. start with index 0
2. Compare each element with target
3. If matches -> return index value
4. If not (else) -> move to the next element 
5. If reaches end -> element not found

algorithm:
1. 2 pointer
    low = 0
high = n-1
2. mid (low+high)//2
3. Compare
if arr[mid] == target
if target<arr[mid] -> search left side
if target>arr[mid] -> search right side
4. Repeat until low = high = mid
'''
arr = list(map(int, inpur("Enter elements:").split()))
target=int(input("Enter element to be searched:"))
found=False
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        print("Element found at index:", mid)
        found=True
        break
    elif target<arr[mid]:
        right=mid-1
    else:
        left=mid+1
if not found:
    print("Elements not found!!!!")

#----- DRY RUN -----
'''
2 4 6 8 10 12
0 1 2 3  4  5

10 
l = 0
r = 5
while 0<5:
m= 5//2=2
arr[2]=6==10
6<10
left = 3
while 3<=5:
l=3
r=5
m= 3+5//2=4
arr[4]==10
10==10'''