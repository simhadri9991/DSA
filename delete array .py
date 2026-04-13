#delete operation in array using pop method

a=[1,2,5,3,4]
print("array before deletion:",a)
a.pop(2)
print("array after deletion:",a)




a=[1,2,5,3,4]
print("array before deletion:",a)
a.remove(2)
print("array after deletion:",a)



n=int(input("Enter the number of elements:"))
a=[]
for i in range(n):
    a.append(int(input("Enter elements:")))
print("Array before deletion:",a)
value=int(input("enter the index value to delete:"))
a.remove(value)
print("Array after deletion",a)    