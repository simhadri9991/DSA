#jump search
'''sorted arrays
2 4 6 8 10 12 14 16 18
0 1 2 3  4   5  6  7  8
target=16
len(arr)=9
squareroot(9)=3

2 4 6       8 10 12         14 16 18
  1            4                7
  target = 2==16
  target = 8==16
  target = 14==16
  initial +=1
  target =1= 4==16
  target =4= 10==16
  target =7= 16==16
  algorithm:
  1.choose step size = squareroot(n)
  2.Jump for all divided steps
  3.Stop when
  element is greater/ end of array each
  '''
import math
arr=list(map(int,input("Enter elements:").split()))
target=int(input("Enter element to be sorted:"))
n= len(arr)
step= int(math.sqrt(n))
i=0
while i<n and arr[min(i+step, n)-1]<target:
    i+=step
for j in range(i, min(i+step, n)):
    if arr[j]==target:
        print("Found at index", i)
        break
else:
    print("Not found!!!")
