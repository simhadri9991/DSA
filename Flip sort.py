'''6  8  5 6 1 5 3 1
   1  7  2 3 5 1 2 2
   7  1  3 2 2 2 2 2
   8  6  6 5 3 3 1 3
   3  1  1 6 6 6 6 6
   2  2 7 7 7 7 7 7 
   5  5 8 8 8 8 8 8
   n-1   n-2 n=3 n=4

   aproach:
   1.find the max element in the unsorted array
   2.bring it to the zero index value followd by respective values
   3.then flip the total array to thr correct position for array of size n:
   4.start for last index(n-1)
   repeat
   -find index max(0->i)
   -flip from 0-> max_index
   -flip from 0->max_index
   -flip 0-> i
''' 
# Flip sort / Pancake Sort
def flip(arr, k):
    start = 0
    while start < k:
        arr[start], arr[k] = arr[k], arr[start]
        start += 1
        k -= 1 # Corrected decrement inside the loop

def pancake(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        max_index = 0
        for j in range(1, i + 1):
            if arr[j] > arr[max_index]:
                max_index = j
        
        if max_index != i:
            # Flip max to the front
            if max_index != 0:
                flip(arr, max_index)
            # Flip max to its correct sorted position
            flip(arr, i)
    return arr

arr = list(map(int, input("Enter the elements: ").split()))
sorted_array = pancake(arr)
print("Sorted array:", sorted_array)