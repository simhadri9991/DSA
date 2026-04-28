#operations

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
def insert_end(data):
    global head
    newnode=node(data)
    newnode.next=head
    head=newnode
#testing (Create Cycle)

def Create_Cycle(pos):
    global head
    if pos==-1:
        return
    temp=head
    cycle_node=None
    index=0
    while temp.next:
        if index==pos:
            cycle_node=temp
        temp=temp.next
        index +=1
    if cycle_node:
        temp.next=cycle_node
def detect_cycle():
    slow=head
    fast=head
    while fast and fast.next:
      slow=slow.next
      fast=fast.next.next
    if slow==fast:
        print("Cycle detected")
        return
    print("No cycle detected........")
  
def display(limit=15):
    temp=head
    count=0
    while temp and count<limit:
        print(temp.data,end="->")
        temp=temp.next
        count+=1
    print("......" if temp else "None")

n=int(input("Enter number of nodes:"))                         
for _ in range(n):
    val=int(input("Enter value:"))
    insert_end(val)
print("\n Linked List:")
display()
pos=int(input("Enter a position"))
Create_Cycle(pos)
detect_cycle()
display()