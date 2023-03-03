from leetcode_alg import *


class Solution:
    def getDirections(self, root: TreeNode,
                      startValue: int, destValue: int) -> str:
        root = find_common_ancestor(root, {startValue, destValue})
        path2s = bytearray()
        path2d = bytearray()
        find_path(root, startValue, path2s)
        find_path(root, destValue, path2d)
        path2d = path2d.decode()
        return "U" * len(path2s) + path2d


class Solution2:
    def getDirections(self, root: TreeNode,
                      startValue: int, destValue: int) -> str:
        path2s = bytearray()
        path2d = bytearray()
        find_path(root, startValue, path2s)
        find_path(root, destValue, path2d)
        idx = find_prefix(path2s, path2d)
        #
        path2d = path2d[idx:].decode()
        return "U" * len(path2s[idx:]) + path2d


if __name__ == "__main__":
    root = "[5,1,2,3,null,6,4]"
    root = to_tree(root)
    print(Solution().getDirections(root, 3, 6))
    print(Solution2().getDirections(root, 3, 6))
