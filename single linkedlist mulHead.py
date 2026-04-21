# Insert multiple values from the beginning(Head) in a single linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
def insertbegin(data):
    global head
    newnode= node(data)
    newnode.next=head
    head=newnode
n=int(input("Enter number of nodes: "))
for _ in range(n):
    val=int(input("Enter value"))
    insertbegin(val)
temp= head
print("Linkedlist:")
while temp:
    print(temp.data, end="->")
    temp= temp.next
print("Tail")