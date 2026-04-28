#replace element in a singly linked list
#Operations
def search(key):
    temp = head
    position = 1
    while temp:
        if temp.data == key:
            print("Element found in node:", position)
            return  # Stop once found
        
        # FIXES START HERE:
        temp = temp.next  # Move to next node (Prevents Infinite Loop)
        position += 1     # Update position counter
    
    print("Element not found") # Let user know if search failed
            

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
    insert_begin(val)
print("\n Linked List:")
display()
old= int(input("enter value to replace :"))
new= int(input("enter new value :"))
replace(old, new)
print("\n updated list:")
display()