
from leetcode_alg import *


def dfs(root: TreeNode, targetSum: int) -> bool:
    targetSum -= root.val
    if root.left is None and root.right is None:
        return targetSum == 0
    #
    if root.left and dfs(root.left, targetSum):
        return True
    if root.right and dfs(root.right, targetSum):
        return True
    return False


class Solution:
    """recommended"""

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return dfs(root, targetSum)


class Solution2:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        stack = [(root, targetSum)]
        while len(stack) > 0:
            tn, t = stack.pop()
            t -= tn.val
            if tn.left is None and tn.right is None and t == 0:
                return True
            #
            if tn.right:
                stack.append((tn.right, t))
            if tn.left:
                stack.append((tn.left, t))
        return False


if __name__ == "__main__":
    root = to_tree("[5,4,8,11,null,13,4,7,2,null,null,null,1]")
    targetSum = 22
    assert Solution().hasPathSum(root, targetSum) is True
    assert Solution2().hasPathSum(root, targetSum) is True
