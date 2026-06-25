from typing import Union

class ListNode:
    def __init__(self, val: int, next: Union[ListNode, None] = None) -> None:
        self.val : int = val
        self.next: Union[None, ListNode]  = next
        
    def __repr__(self) -> str:
        return "ListNode({} {})".format(self.val, self.next is not None)