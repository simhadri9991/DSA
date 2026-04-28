class node:
    def __init__(self,data):
        self.data = data
        self.next = None
def insert_begin(head, data):
    new = node(data)
    if head is None:
        new.next = new
        return new
    temp = head
    while temp.next != head:
        temp = temp.next
    new.next = head
    temp.next = new
    head = new
    return head
def display(head):
    if head is None:
        return
    temp = head
    while True:
        print(temp.data, end="->")
        temp = temp.next
        if temp == head:
            print(temp.data)
            break
head = None
n = int(input("Enter the number of nodes:"))
for _ in range(n):
    val = int(input("Enter the value:"))
    head = insert_begin(head, val)
display(head)