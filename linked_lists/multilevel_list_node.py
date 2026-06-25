class MultiLevelListNode:
    def __init__(self, val:int, next: MultiLevelListNode, child: MultiLevelListNode) -> None:
        self.val = val
        self.next: MultiLevelListNode | None = next
        self.child: MultiLevelListNode | None = child