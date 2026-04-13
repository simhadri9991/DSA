#for string
'''arr=input("enter elements with spaces:").split()
search=(input("enter the element to be searched:"))
found= False
for i in range(len(arr)):
    if arr[i]== search:
        print("elements found at index:", i)
        found = True
        break
if not found:
    print("Elements not found!!!!!")'''

arr=list(map(int,input("enter an element with spces").split()))
search=int(input("enter the element to be searched:"))
found= False
for i in range(len(arr)):
    if arr[i]> search:
        print("elements found at index:", i)
        found = True
        break
if not found:
    print("Elements not found!!!!!")