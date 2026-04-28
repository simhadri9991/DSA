class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
head=None
def insert(data):
    global head
    newnode=node(data)
    newnode.next=head
    head=newnode
def replace(old,new):
    temp=head
    found=False
    while temp:
        if temp.data==old:
            temp.data=new
            found-True
        temp=temp.next
    if found:
        print("Replaced",old,"with",new)
    else:
        print("Vlue not found in SLL")
def display():
    temp= head
    while temp:
        print(temp.data,end ="->")
        temp=temp.next
    print("Tail") 
n=int(input("Enter number of nodes:"))
for _ in range(n):
    val=int(input("Enter value:"))
    insert(val)
print("\n Linked list: ")
display()
old=int(input("Enter value to replace:"))
new=int(input("Enter new value:"))
replace(old, new)
print("\n Updated list")
display()