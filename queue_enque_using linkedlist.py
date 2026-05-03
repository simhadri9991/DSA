#enqueue using linkedlist
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
front=rear=None
n=int(input("enter the size of the queue:"))
for i in range(n):
    val=int(input("Enter the value :"))
    new=node(val)
    if front is None:
        front=rear=new
    else:
        rear.next=new
        rear=new
temp=front
print("queue after enqueue :",end=" ")
while temp:
    print(temp.data,end=' ')
    temp=temp.next