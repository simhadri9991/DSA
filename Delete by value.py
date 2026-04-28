#delete by value in a doubly linked list
class node:
    def __init__(self,data):
        self.data= data
        self.next= None
        self.prev= None

def delete_value(head,key):
    temp=head
    while temp:
        if temp.data==key:
            if temp.prev==None:
                head=temp.next
                if head:
                    head.prev=None
                return head
            if temp.next==None:
                temp.prev.next=temp.next
                temp.next.prev=temp.prev
            temp=temp.next
    return head   
def display(head):
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next             
head= None
n= int(input("enter number of nodes:"))
for _ in range(n):
    val= int(input("enter the value:"))
    if head is None:
        head= node(val)
    else:
        temp= head
        while temp.next:
            temp=  temp.next
        new= node(val)
        temp.next= new
        new.prev= temp
key= int(input("enter the value u wanna delete:"))
head=delete_value(head,key)
display(head)