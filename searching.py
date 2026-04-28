#Operations
class node:
    def __init__(self, data):
        self.data= data
        self.next= None
head= None
def insert(data):
    global head
    newnode= node(data)
    newnode.next= head
    head= newnode
def search(key):
    temp= head
    position= 1
    while temp:
        if temp.data==key:
            print("Element found in node:",position)
            return
        temp= temp.next
        position+=1
    print("No node reflects the key....")
def display():
    temp=head
    while temp:
        print(temp.data,end ="->")
        temp=temp.next
    print("None")

n=int(input("Enter number of nodes:"))
for _ in range(n):
    val=int(input("Enter value:"))
    insert(val)
print("Inserted linkedlist:")
display()
key=int(input("Enter the value of node to be deleted"))
delete(key)
print("\n Updated Linkedlist:")
display()
print("None")