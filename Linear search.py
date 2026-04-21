'''
Types of searching 
1. Linear search
2. Binary search
3. Jump search

11 22 33 55 21
0   1  2  3  4 
target = 55
algorithm:
1. Start with index 0
2. Compare each element with target
3. If matches -> return index value
4. If not (else) -> move to the next element
5. If reches end -> element not found
'''
arr = list(map(int, input("Enter elements:").split()))
target = int(input("Enter element to be searched:"))
found = False
for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index:", i)
        found = True
        break
if not found:
    print("Element not found !!!!")