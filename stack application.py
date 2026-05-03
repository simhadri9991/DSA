#applications of stack for redo and undo operations
 
undo_stack=[]
redo_stack=[]

undo_stack.append("India")
undo_stack.append("Brazil")
undo_stack.append("China")
print("Current Stack:",undo_stack)
if len(undo_stack)>0:
    action = undo_stack.pop()
    undo_stack.append(action)
    print("Undo:",action)
print("Current stack",undo_stack)
if len(redo_stack)>0:
    action=redo_stack.pop()
    undo_stack.append(action)
    print("redo",action)
print("Redo stack",redo_stack)