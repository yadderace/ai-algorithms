from queue import PriorityQueue

def peek_from_queue(myqueue, node_id):
    
    temp_queue = PriorityQueue()
    node = None

    while not myqueue.empty():
        priority, obj = myqueue.get()

        if obj.node_id == node_id:
            # Found the object, put it back into the original queue
            node = obj
            myqueue.put((priority, obj))
            break
        else:
            # Not the target object, put it into the temporary queue
            temp_queue.put((priority, obj))

    # Restore the elements in the temporary queue back to the original queue
    while not temp_queue.empty():
        priority, obj = temp_queue.get()
        myqueue.put((priority, obj))

    return node

def update_priority(myqueue, node_id, new_priority):

    temp_queue = PriorityQueue()
    node = None
    
    while not myqueue.empty():
        priority, obj = myqueue.get()

        if obj.node_id == node_id:
            # Found the object, put it back into the original queue
            node = obj
            myqueue.put((priority, obj))
            break
        else:
            # Not the target object, put it into the temporary queue
            temp_queue.put((priority, obj))

    # Restore the elements in the temporary queue back to the original queue
    while not temp_queue.empty():
        priority, obj = temp_queue.get()
        myqueue.put((priority, obj))

    if node != None:
        myqueue.put((new_priority, node))