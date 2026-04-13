''' Arrange strings according to their lenv Descending order '''

n=int(input("Enter the value:"))
a=[]
for i in range(n):
    ele=input("enter names")
    a.append(ele)
print("unsorted array:",a)
a.sort(key=lambda x:len(x),reverse=True)
print("sorted array:",a)