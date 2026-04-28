#Double linkedlist
#insert at postion
def insert_at_position(head,data,pos):
    newnode=node(data)

    if pos==1:
        if head:
            head.prev=newnode
            newnode.next=head
        return newnode

    temp=head

    for _ in range(pos-2):
        if temp is None:
            return head
        temp=temp.next

    if temp is None:
        return head

    newnode.next=temp.next

    if temp.next:
        temp.next.prev=newnode

    temp.next=newnode
    newnode.prev=temp

    return head