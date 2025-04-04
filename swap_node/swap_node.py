def swap_pairs(head):
    if not head or not head.next:
        return head
    new_head = head.next
    head.next = swap_pairs(new_head.next)
    new_head.next = head
    
    return new_head