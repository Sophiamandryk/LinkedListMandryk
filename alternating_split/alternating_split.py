class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def alternating_split(head):
    if not head or not head.next:
        raise ValueError("The list must contain at least two nodes.")
    
    first_head = None
    second_head = None
    first_tail = None
    second_tail = None
    
    current = head
    index = 0
    
    while current:
        new_node = Node(current.data)
        if index % 2 == 0: 
            if not first_head: 
                first_head = new_node
                first_tail = new_node
            else:
                first_tail.next = new_node
                first_tail = new_node
        else: 
            if not second_head: 
                second_head = new_node
                second_tail = new_node
            else:
                second_tail.next = new_node
                second_tail = new_node
        
        current = current.next
        index += 1

    return Context(first_head, second_head)
