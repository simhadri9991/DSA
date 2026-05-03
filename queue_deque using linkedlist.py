#Dequeue using linkedlist
'''class node:
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
if front is None:
    print("Queue Empty/Underflow!!!")
else:
    removed=front.data
    front=front.next
    if front is None:
        rear=None
    print("Dequeued element :",removed)
temp=front
print("queue after enqueue :",end=" ")
while temp:
    print(temp.data,end=' ')
    temp=temp.next'''

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
if front is None:
    print("Queue Empty/Underflow!!!")
else:
    print("front Element:",front.data)