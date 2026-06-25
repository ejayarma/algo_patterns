from list_node import ListNode
from typing import Union

def linked_list_reversal(head: Union[ListNode, None]) -> Union[ListNode, None]: 
    if not head:
        return head
    curr_node, prev_node = head, None
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        
        prev_node = curr_node
        curr_node = next_node

    return prev_node

def linked_list_reversal_recursion(head: Union[ListNode, None]) -> Union[ListNode, None]:
    if (not head) or (not head.next):
        return head
    
    new_head = linked_list_reversal_recursion(head.next)
    head.next.next = head
    head.next = None
    
    return new_head

def print_linked_list(head: Union[ListNode, None]):
    curr_node = head
    while curr_node:
        if curr_node.next:
            print(curr_node.val, end=' -> ')
        else:
            print(curr_node.val, end='\r\n')
        curr_node = curr_node.next


node7 = ListNode(70, None)
node6 = ListNode(60, node7)
node5 = ListNode(50, node6)
node4 = ListNode(40, node5)
node3 = ListNode(30, node4)
node2 = ListNode(20, node3)
node1 = ListNode(10, node2)


print_linked_list(node1)


print_linked_list(linked_list_reversal_recursion(node1))

