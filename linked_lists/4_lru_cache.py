from doubly_linked_list_node import DoublyLinkedListNode
from typing import Union

class LRUCache:
    
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        
        self.hash_map: dict[int, DoublyLinkedListNode] = {}
        self.head = DoublyLinkedListNode(-1, -1)
        self.tail = DoublyLinkedListNode(-1, -1)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_tail(self, node: DoublyLinkedListNode) -> None:
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        
        if prev_node:
            prev_node.next = node
        self.tail.prev = node
        
    def remove_node(self, node: DoublyLinkedListNode | None) -> None:
        if node and node.prev:
            node.prev.next = node.next
        if node and node.next:
            node.next.prev = node.prev
        
        
    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        
        self.remove_node(self.hash_map[key])
        self.add_to_tail(self.hash_map[key])
        
        return self.hash_map[key].val

    def put(self, key: int, val: int) -> None:
        
        if key in self.hash_map:
            self.remove_node(self.hash_map[key])
            
        node = DoublyLinkedListNode(key, val)
        self.hash_map[key] = node
        
        if len(self.hash_map) > self.capacity:
            self.remove_node(self.head.next)
            if self.head.next:
                del self.hash_map[self.head.next.key]

        self.add_to_tail(node)

        
        