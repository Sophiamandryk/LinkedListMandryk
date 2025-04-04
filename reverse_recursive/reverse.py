def reverse(head):
    if not head or not head.next:
        return head
    reversed_list = reverse(head.next)
    head.next.next = head
    head.next = None
    
    return reversed_list