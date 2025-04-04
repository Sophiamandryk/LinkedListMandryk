def get_nth(node, index):
    count = 0
    current_node = node
    while current_node is not None:
        if count == index:
            return current_node
        count += 1
        current_node = current_node.next
    raise IndexError()
# head = Node(1, Node(2, Node(3)))
# print(get_nth(head, 2))
