
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
            r, t = stack.pop()
            t -= r.val
            if r.left is None and r.right is None and t == 0:
                return True
            #
            if r.right:
                stack.append((r.right, t))
            if r.left:
                stack.append((r.left, t))
        return False


if __name__ == "__main__":
    root = to_tree("[5,4,8,11,null,13,4,7,2,null,null,null,1]")
    targetSum = 22
    print(Solution().hasPathSum(root, targetSum))
    print(Solution2().hasPathSum(root, targetSum))
