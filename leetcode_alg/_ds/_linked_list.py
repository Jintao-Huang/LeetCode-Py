# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *
_T = TypeVar("_T")


class LinkedListNode(Generic[_T]):
    def __init__(self, val: _T, prev: Optional["LinkedListNode[_T]"] = None,
                 next: Optional["LinkedListNode[_T]"] = None) -> None:
        self.val = val
        self.prev: "LinkedListNode[_T]" = prev
        self.next: "LinkedListNode[_T]" = next


class LinkedList(Generic[_T]):
    def __init__(self, nums: Optional[List[_T]] = None) -> None:
        self.head = LinkedListNode[_T](0)
        self.tail = LinkedListNode[_T](0, self.head, self.head)
        self.head.prev, self.head.next = self.tail, self.tail
        if nums is not None:
            for val in nums:
                lln = LinkedListNode(val)
                self.insert_between(self.tail.prev, lln, self.tail)

    @staticmethod
    def insert_between(node: LinkedListNode[_T], new_node: LinkedListNode[_T],
                       node_next: LinkedListNode[_T]) -> None:
        """node <-> node_next"""
        node.next, new_node.next = new_node, node_next
        node_next.prev, new_node.prev = new_node, node

    @staticmethod
    def remove(node: LinkedListNode[_T]) -> None:
        node_prev, node_next = node.prev, node.next
        node_prev.next, node_next.prev = node_next, node_prev

    def __repr__(self) -> str:
        res = []
        lln = self.head.next
        tail = self.tail
        while lln is not tail:
            res.append(lln.val)
            lln = lln.next
        return f"{self.__class__.__name__}({res!r})"
