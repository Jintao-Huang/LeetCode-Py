# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *
from .._lc._lc_ds import ListNode


def reverse_list(head: ListNode, tail_next: Optional[ListNode]) -> ListNode:
    ln = head
    prev = tail_next
    while ln != tail_next:
        ln_next = ln.next
        ln.next = prev
        prev = ln
        ln = ln_next
    return prev


def find_mid_node(head: Optional[ListNode]) -> ListNode:
    """[1,2,3,4,5]返回[3,4,5]; [1,2,3,4]返回[3,4]"""
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def find_last_kth_node(head: Optional[ListNode], k: int) -> ListNode:
    lo, hi = head, head
    for _ in range(k):
        hi = hi.next
    while hi:
        lo = lo.next
        hi = hi.next
    return lo
