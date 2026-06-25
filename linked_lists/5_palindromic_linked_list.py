from list_node import ListNode

def find_middle(head: ListNode) -> ListNode | None:
    slow = fast = head
    while fast and fast.next:
        if slow:
            slow = slow.next
        fast = fast.next.next
        
    return slow

def reverse_linked_list(head: ListNode | None) -> ListNode | None:
    current_node = head
    previous_node = None
    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
        
    return previous_node

def palindromic_linked_list(head: ListNode | None) -> bool:
    if not head:
        return False
    
    mid = find_middle(head)
    
    new_head = reverse_linked_list(mid)
    
    while new_head and new_head.next:
        if head and new_head and head.val != new_head.val:
            return False
    
        if head:
            head = head.next
        new_head = new_head.next

    return True
