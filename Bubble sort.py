'''
Bubble sorting - Adjacent value sorting
1. arr[0]>arr[i+1]
2. a[0]!>arr[i+1]
'''
arr = list(map(int,input("Enter elements:").split()))
n = len(arr)
for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] == arr[j+1], arr[j]
print("Sorted array",arr)

#-------- Dry Run ---------
'''
arr = [5,3,8,4,2]
n=5
1. i=0
2. j=0->3
j=0,1,2,3
arr[0]>arr[1]
5>3
3 5 8 4 2
j=1
arr[1]>arr[2]
5>8 F
3 5 8 4 2
j=2
arr[2]>arr[3]
8>4 T
3 5 4 8 2
j=3
arr[3]>arr[4]
8>2 T
3 5 4 2 8

i=1, 2nd iteration
j -> 0 to 2
j=0
3>5 F
j=1
5>4 T
3 4 5 2 8

i=2 3rd iteration
j -> 0 to 1
j=0
3>4 F
j=1
4>2 T
3 2 4 5 8

i=3 4th iteration
i=0
3>2
2 3 4 5 8

i=4 5th iteratoion
j: 0 -> -1
'''