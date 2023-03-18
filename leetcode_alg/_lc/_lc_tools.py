
from .._types import *
from ._lc_ds import ListNode, TreeNode
from inspect import getmembers, isfunction, ismethod
import json


def to_linkedlist(_list: List[int]) -> Optional[ListNode]:
    head = ListNode()
    cur = head
    for x in _list:
        cur.next = ListNode(x)
        cur = cur.next
    return head.next


def from_linkedlist(ll: Optional[ListNode]) -> List[int]:
    res = []
    while ll:
        res.append(ll.val)
        ll = ll.next
    return res


def to_tree(l_s: str) -> Optional[TreeNode]:
    tn_l: List[Optional[int]] = json.loads(l_s)
    n = len(tn_l)
    if n == 0:
        return None
    #
    root = TreeNode(tn_l[0])
    dq = Deque[TreeNode]([root])
    idx = 1
    while dq:
        if idx >= n:
            break
        tn_p = dq.popleft()
        lc = tn_l[idx]
        if lc is not None:
            dq.append(TreeNode(lc))
            tn_p.left = dq[-1]
        idx += 1
        #
        if idx >= n:
            break
        rc = tn_l[idx]
        if rc is not None:
            dq.append(TreeNode(rc))
            tn_p.right = dq[-1]
        idx += 1
    return root


def from_tree(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    dq = Deque[TreeNode]([root])
    res: List[Optional[int]] = [root.val]
    while dq:
        tn = dq.popleft()
        lc, rc = tn.left, tn.right
        if lc is None:
            res.append(None)
        else:
            res.append(lc.val)
            dq.append(lc)
        if rc is None:
            res.append(None)
        else:
            res.append(rc.val)
            dq.append(rc)
    #
    while res[-1] is None:  # res[0]一定不是None
        res.pop()
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
        r = callable_fc(*args)  # res
        if isinstance(callable_fc, type):  # class
            mapper.update(getmembers(r, predicate=lambda obj:
                                     ismethod(obj) or isfunction(obj)))
        res.append(r)
    return res
