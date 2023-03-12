
from leetcode_alg import *


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return find_mid_node(head)


if __name__ == "__main__":
    head = to_linkedlist([1, 2, 3, 4, 5])
    assert from_linkedlist(Solution().middleNode(head)) == [3, 4, 5]
