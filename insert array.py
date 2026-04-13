#insert operation in array using character array

a=['a','b','d','e','f']
print("before insertion:",a)
index=2
value='c'
a.insert(index,value)
print("after insertion:",a)




#insert operation in array using character array with user inout

n=int(input("size of array:"))
a=[]
for i in range(n):
    a.append(input("Enter the element:"))
print("array before insertion is:",a)
index=int(input("enter index value to insert"))
value=input("enter the value")
a.insert(index,value)
print("after the insertion:",a)    