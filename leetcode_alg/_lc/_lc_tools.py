
from typing import List, Any, Dict
from inspect import getmembers, isfunction, ismethod
from ._lc_ds import *


def to_linkedlist(l: List[int]) -> Optional[ListNode]:
    head = ListNode()
    cur = head
    for x in l:
        cur.next = ListNode(x)
        cur = cur.next
    return head.next


def from_linkedlist(ll: Optional[ListNode]) -> List[int]:
    res = []
    while ll is not None:
        res.append(ll.val)
        ll = ll.next
    return res


def call_callable_list(
    callable_list: List[str],
    args_list: List[List[Any]],
    mapper: Dict[str, Any],  # map callable str to callable function/class
) -> List[Any]:
    res = []
    mapper = mapper.copy()
    for callable_str, args in zip(callable_list, args_list):
        callable_fc = mapper[callable_str]  # callable function/class
        r = callable_fc(*args)
        if isinstance(callable_fc, type):  # class
            mapper.update(getmembers(r, predicate=lambda obj:
                                     ismethod(obj) or isfunction(obj)))
        res.append(r)
    return res
