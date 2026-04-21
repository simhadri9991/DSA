# Insert from beginning in a single linked list
class node:
    def __init__(self, data):
        self.data=data
        self.next=None
n=int(input("Enter number of nodes: "))
head = None
for i in range(n):
    val=int(input("Enter the value: "))
    newnode=node(val)
    if head is None:
        head= newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
x=int(input("Enter values to insert at beginning:"))
newnode= node(x)
newnode.next=head
head=newnode
print("Linkedlist", end=" ")
temp= head
while temp:
    print(temp.data, end="->")
    temp= temp.next
print("None")