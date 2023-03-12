
from leetcode_alg import *


def dfs(root: TreeNode, res: List[int]) -> int:
    if root.left is None and root.right is None:
        res[0] = max(res[0], root.val)
        return root.val
    #
    left, right = 0, 0
    if root.left:
        left = max(left, dfs(root.left, res))
    if root.right:
        right = max(right, dfs(root.right, res))
    res[0] = max(res[0], left+right+root.val)
    return max(left, right) + root.val


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res = [root.val]
        dfs(root, res)
        return res[0]


if __name__ == "__main__":
    root = to_tree("[-10,9,20,null,null,15,7]")
    assert Solution().maxPathSum(root) == 42
