from leetcode_alg import *


def dfs(root: TreeNode, targetSum: int, path: List[int], res: List[List[int]]) -> None:
    targetSum -= root.val
    path.append(root.val)
    if targetSum == 0 and root.left is None and root.right is None:
        res.append(path.copy())
    else:
        if root.left:
            dfs(root.left, targetSum, path, res)
        if root.right:
            dfs(root.right, targetSum, path, res)
    path.pop()


class Solution:
    """faster"""

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        res: List[List[int]] = []
        dfs(root, targetSum, [], res)
        return res


def dfs2(root: TreeNode, targetSum: int, path: List[int], res: List[List[int]]) -> None:
    targetSum -= root.val
    left, right = root.left, root.right
    if left is None and right is None and targetSum == 0:
        res.append(path.copy())
        return
    if left:
        path.append(left.val)
        dfs2(left, targetSum, path, res)
        path.pop()
    if right:
        path.append(right.val)
        dfs2(right, targetSum, path, res)
        path.pop()


class Solution2:
    """都是回溯写法, 只是风格不同. """

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        res: List[List[int]] = []
        dfs2(root, targetSum, [root.val], res)
        return res


if __name__ == "__main__":
    root = to_tree("[5,4,8,11,null,13,4,7,2,null,null,5,1]")
    targetSum = 22
    print(Solution().pathSum(root, targetSum))
    print(Solution2().pathSum(root, targetSum))
