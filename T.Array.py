'''Traversal an array'''
arr= list(map(int, input("Enter numbers:").split()))
for i in range(len(arr)):
    print(arr[i]+1, end="->")
#Dry-Run
'''
1.Fixed size
2.Same data type
3.Access through index
4.Contiguous memory

arr=[12,13,14,15]
arr=[2]
arr=[-2]

2- -1 0 1 2

arr=[12,13,14,15]
len(arr)=4
for 0->3
arr[0]+1=11+1=12
arr[1]+1=12+1=13
arr[2]+1=13+1=14
arr[3]+1=14+1=15
'''
