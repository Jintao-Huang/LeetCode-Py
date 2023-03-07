
from leetcode_alg import *


class Solution:
    def reverseBetween(self, head: Optional[ListNode], 
                       left: int, right: int) -> Optional[ListNode]:
        head = ListNode(0, head)
        lo, hi = head, head
        for _ in range(left-1):
            lo = lo.next
        for _ in range(right+1):
            hi = hi.next
        # 
        lo.next = reverse_list(lo.next, hi)
        return head.next
    
if __name__ == "__main__":
    head = to_linkedlist([1, 2, 3, 4, 5])
    print(from_linkedlist(Solution().reverseBetween(head, 2, 4)))
