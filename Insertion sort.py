'''
Insertion sort(Algorithm)
1. Start from second value assuming 1st index value as sorted
for i-> 1 to n-1
2. pick the current element as key
key = arr[i]
3. compare with previous element
while j>=0 and arr[j]>key
4. Shift all the larger elements to the right
arr[j+1] = arr[j]
5. Insert the key in position
6. repeat till sorted
'''
arr = list(map(int, input("Enter elements:").split()))
for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j>=0 and arr[j]>key:
        arr[j+1] = arr[j]
        j = -1
        arr[j+1] = key
print("sorted elements:", arr)

#------ Dry Run ------
'''
5 3 4 1
1st iteration i=0
key = arr[1]=3
j = 0
arr[0] > 3
    5>3
[5,5,4,1]
    j=-1
arr[0]-3
[3,5,4,1]
    i=2
key = 4
j = 1
5>4
[3,5,5,1]
j = 0
arr[1]=4
[3,4,5,1]
3>4 F
arr[1]=4
[3,4,5,1]
i = 3
key = 1
j = 2
5>1
[3,4,5,5]
j=1
arr[2]=1
[3,4,1,5]
j=1
arr[1]>1
4>1
[3,4,4,5]
j=0
arr[1]=key=1
[3,1,4,5]
3>1
[3,3,4,5]
j=-1
arr[0]=1
[1,3,4,5]
'''