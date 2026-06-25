class DoublyLinkedListNode:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev: DoublyLinkedListNode | None = None
        self.next: DoublyLinkedListNode | None = None
        

    