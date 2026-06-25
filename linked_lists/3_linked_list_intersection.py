from list_node import ListNode
from typing import Union

def linked_list_intersection(head_A: Union[ListNode, None], head_B: Union[ListNode, None]) -> Union[ListNode, None]:
    ptr_A, ptr_B = head_A, head_B
    
    while ptr_A and  ptr_A != ptr_B:
        ptr_A = ptr_A.next if ptr_A else head_B
        ptr_B = ptr_B.next if ptr_B else head_A
        
    return ptr_A
