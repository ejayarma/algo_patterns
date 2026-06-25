from linked_lists.list_node import ListNode

def linked_list_midpoint(head: ListNode) -> ListNode | None:
    slow = fast = head
    
    while fast and fast.next:
        if slow:
            slow = slow.next
        fast = fast.next.next

    return slow
