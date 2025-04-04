class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
def linked_list_from_string(s):
    if s.strip() in {"null", "NULL", "nil", "nullptr", "null()"}:
        return None
    nodes = s.split(" -> ")
    nodes.pop()
    head = None
    for value in reversed(nodes):
        head = Node(int(value), head)
    return head