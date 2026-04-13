n=int(input("Enter the value: "))
a=[]
for i in range(n):
    ele=input("Enter name: ")
    a.append(ele)
print("Unsorted array:",a)
a.sort(key=lambda x: len(x))
print("Sorted array:",a)