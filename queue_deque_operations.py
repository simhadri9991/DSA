#dequeue Operation
queue = list(map(int, input("enter the queue elements:").split()))
if len(queue) == 0:
    print("queue is empty...underflow")
else:
    removed = queue.pop(0)
    print("dequeue element:", removed)
    print("remaining elements:", queue)
    print("peek element:", queue[0])
    print("size of queue:", len(queue))