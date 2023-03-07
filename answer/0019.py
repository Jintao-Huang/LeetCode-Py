
from leetcode_alg import *


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        head = ListNode(0, head)
        ln = find_last_kth_node(head, n+1)
        ln.next = ln.next.next
        return head.next


if __name__ == "__main__":
    head = to_linkedlist([1, 2, 3, 4, 5])
    print(from_linkedlist(Solution().removeNthFromEnd(head, 2)))
