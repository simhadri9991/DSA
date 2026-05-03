#application of stack for menu diriven operations
undo_stack =[]
redo_stack =[]
while True:
    print("\n. Perform action")
    print("2. Undo")
    print("3. Redo")
    print("4. Display")
    print("5. Exit")
    choice=int(input("Enter your choice :"))
    if choice==1:
        action=input("enter action :")
        undo_stack.append(action)
        redo_stack.clear()
        print("Action Performed ",action)
    elif choice==2:
        if len(undo_stack)==0:
            print("Undo STack is Empty !!!!")
        else:
            action=undo_stack.pop()
            redo_stack.append(action)
            print("Undo",action)
    elif choice==3:
        if len(redo_stack)==0:
            print("Redo stack is empty !!!!")
        else:
            action=redo_stack.pop()
            undo_stack.append(action)
            print("Redo",action)
    elif choice==4:
        print("Undo stack :",undo_stack)
        print("Redo Stack :",redo_stack)
    elif choice==5:
        break
    else:
        print("Invalid Choice.....Try again ")