# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from ..._types import *
from .._linked_list import LinkedListNode, LinkedList
_K, _V = TypeVar("_K"), TypeVar("_V")


class OrderedDict(Generic[_K, _V]):
    """已由collections.OrderedDict(C)实现. 生产情况下请勿使用此类, 仅用于学习"""

    def __init__(self, _dict: Optional[Dict[_K, _V]] = None) -> None:
        """dict在py>=3.7更改: 字典顺序会确保为插入顺序
        ref: https://docs.python.org/zh-cn/3/library/stdtypes.html"""
        self.ll = LinkedList[Tuple[_K, _V]]()
        self.dict: Dict[_K, LinkedListNode[Tuple[_K, _V]]] = {}
        if _dict is not None:
            for k, v in _dict.items():
                self.setitem(k, v)

    def pop(self, k: _K) -> _V:
        lln = self.dict.pop(k)
        self.ll.remove(lln)
        return lln.val[1]

    def move_to_end(self, k: _K, last: bool = True):
        lln = self.dict[k]
        self.ll.remove(lln)
        if last:
            n2 = self.ll.tail
            n1 = n2.prev
        else:
            n1 = self.ll.head
            n2 = n1.next
        self.ll.replace_between(n1, lln, n2)

    def popitem(self, last: bool = True):
        if last:
            lln = self.ll.tail.prev
        else:
            lln = self.ll.head.next
        self.ll.remove(lln)
        k, v = lln.val
        self.dict.pop(k)
        return k, v

    def getitem(self, k: _K) -> _V:
        lln = self.dict[k]
        return lln.val[1]

    def setitem(self, k: _K, v: _V) -> None:
        if k in self.dict:
            lln = self.dict[k]
            lln.val = (k, v)
        else:
            lln = LinkedListNode((k, v))
            tail = self.ll.tail
            self.ll.replace_between(tail.prev, lln, tail)
            self.dict[k] = lln

    def __repr__(self) -> str:
        res = []
        lln = self.ll.head.next
        tail = self.ll.tail
        while lln is not tail:
            res.append(lln.val)
            lln = lln.next
        return f"{self.__class__.__name__}({res!r})"
