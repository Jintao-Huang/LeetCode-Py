from leetcode_alg import *


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        return level_order_traversal(root)
if __name__ == "__main__":
    root = to_tree("[3,9,20,null,null,15,7]")
    assert Solution().levelOrder(root) == [[3],[9,20],[15,7]]