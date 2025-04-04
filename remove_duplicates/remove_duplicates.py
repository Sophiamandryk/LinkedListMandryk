class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    if not head:
        return None 
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next   
    return head
# list_head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(4, Node(5)))))))
# result = remove_duplicates(list_head)