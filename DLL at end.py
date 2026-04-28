#Double linked list
#insert at end at DLL
class node:
    def __init__(self,data):
        self.data= data
        self.prev= None
        self.next= None
def insert_end(head, data):
    newnode= node(data)
    if head is None:
        return newnode
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=newnode
    newnode.prev=temp
    return head
def display(head):
    temp= head
    while temp:
        print(temp.data, end="<->")
        temp= temp.next
    print("None")
head=None
n = int(input("eneter number of nodes: "))
for _ in range(n):
    val= int(input("enter value:"))
    head= insert_begin(head, val)
display(head)