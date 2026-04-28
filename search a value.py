#Search a value 

class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def search(head, key):
    temp = head
    pos = 1
    while temp:
        if temp.data == key:
            return pos
        temp = temp.next
        pos += 1
    return -1
head=None
n = int(input("Enter the number of nodes:"))
for _ in range(n):
    val = int(input("Enter the value:"))
    if head is None:
        head = node(val)
    else:
        temp = head
        while temp.next:
            temp = temp.next
        new = node(val)
        temp.next = new
        new.prev = temp
key = int(input("Enter the value your want to search:"))
pos = search(head,key)
if pos != -1:
    print(key, "found at Node:", pos)
else:
    print("Not found")