'''  15 5 24 8 1 13 16 10 20
15 5 24 8 1  3 16 10 20 

15 5 24  8 1     3 16 10 20
15 5 24    8  1    3 16   10 20
   5  15 24       
   15 15 24
   l->15 8 15 24
   r-> 3 10 16 20
   approach:
   1.if array has 1 element then sorted.
   2.if not divide array in 2 halves recursively
   3.after getting independent values sort recursively both halves
   4.merge the 2 sorted arrays

'''
#code:-
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
arr = list(map(int, input("Enter elements:").split()))
sorted_arr=merge_sort(arr)
print("Sorted array", sorted_arr)