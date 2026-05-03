class node:
    def __init__(self,data):
        self.data=data
        self.next=None
front=rear=None
n=int(input("enter the size of the queue:"))
count=0
for i in range(n):
    val=int(input("Enter the value :"))
    new=node(val)
    if front is None:
        front=rear=new
    else:
        rear.next=new
        rear=new
print("size of queue",count)