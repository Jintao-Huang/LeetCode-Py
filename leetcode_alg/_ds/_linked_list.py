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
                self.replace_between(self.tail.prev, lln, self.tail)

    @staticmethod
    def replace_between(node: LinkedListNode[_T], new_node: LinkedListNode[_T],
                       node2: LinkedListNode[_T]) -> None:
        """node <-...-> node2"""
        node.next, new_node.next = new_node, node2
        node2.prev, new_node.prev = new_node, node

    @staticmethod
    def remove(node: LinkedListNode[_T]) -> None:
        node_prev, node_next = node.prev, node.next
        node_prev.next, node_next.prev = node_next, node_prev

    def tolist(self) -> List[_T]:
        res = []
        lln = self.head.next
        tail = self.tail
        while lln is not tail:
            res.append(lln.val)
            lln = lln.next
        return res

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.tolist()!r})"
