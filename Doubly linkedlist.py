#Double linkedlist
#insert at beginning at Dll
class node:
    def __init__(self,data):
        self.data= data
        self.prev= None
        self.next= None
def insert_begin(head, data):
    newnode= node(data)
    if head :
        head.prev= newnode
        newnode.next= head
    return newnode
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