from list_node import ListNode
from typing import Union


def print_linked_list(head: Union[ListNode, None]):
    curr_node = head
    while curr_node:
        if curr_node.next:
            print(curr_node.val, end=' -> ')
        else:
            print(curr_node.val, end='\r\n')
        curr_node = curr_node.next


def remove_kth_last_node_naive(head: ListNode | None, k: int) -> ListNode | None:
    
    dummy = ListNode(-1, head)
    prev_node = dummy
    curr_node = head

    node_bank : list[ListNode] = []
    while curr_node:
        node_bank.append(curr_node)
        curr_node = curr_node.next

    target = node_bank[-k]
    
    curr_node = head

    while curr_node:
        if curr_node.val == target.val and prev_node.next:
            prev_node.next = prev_node.next.next
        
        prev_node = curr_node
        curr_node = curr_node.next
    
    return dummy.next


def remove_kth_last_node(head: ListNode | None, k: int) -> ListNode | None:
    dummy = ListNode(-1, head)
    trailer = leader = dummy
    
    for _ in range(k):
        if leader:
            leader = leader.next
        else:
            return head # k is larger than length of the linked list
        
    while leader and leader.next and trailer:
        trailer = trailer.next
        leader = leader.next
        
    if trailer and trailer.next:
        trailer.next = trailer.next.next
    
    return dummy.next

        

node5 = ListNode(3, None)
node4 = ListNode(7, node5)
node3 = ListNode(4, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

# print_linked_list(node1)


print_linked_list(remove_kth_last_node_naive(node1, 5))
