from leetcode_alg import *


class Solution:
    """中心法"""
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        total = sum(beans)
        res = 0
        for i, x in enumerate(beans):
            z = x * (n-i)
            if z > res:
                res = z
        return total - res

if __name__ == "__main__":
    beans = [4, 1, 6, 5]
    assert Solution().minimumRemoval(beans) == 4
