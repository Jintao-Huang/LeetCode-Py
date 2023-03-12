from leetcode_alg import *


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        carry = 0
        while l1 or l2 or carry != 0:
            x, y = 0, 0
            if l1:
                x = l1.val
                l1 = l1.next
            #
            if l2:
                y = l2.val
                l2 = l2.next
            #
            carry, z = divmod(x+y+carry, 10)
            cur.next = ListNode(z)
            cur = cur.next
        return head.next


if __name__ == "__main__":
    l1 = to_linkedlist([9, 9, 9, 9, 9, 9, 9])
    l2 = to_linkedlist([9, 9, 9, 9])
    assert from_linkedlist(Solution().addTwoNumbers(l1, l2)) == [8,9,9,9,0,0,0,1]
