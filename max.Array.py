'''Find the maximum value'''

arr=list(map(int,input("Enter the numbers:").split()))  # 1 2 3 4
max_value= arr[0]
for i in arr:
    if i>max_value:
        max_value=i
print(max_value)

#Example:-
'''
Enter the numbers:22 33 44 55 66 
66
'''
