b=int(input("Enter a element:"))
a=[]
for i in range(n):
    a.append(int(input("Enter the element{}:")))
    print("array before insertion:",a)
    index=2
    value=10
    a.insert(index,value)
    print("array after insertion:")
