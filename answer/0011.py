
from leetcode_alg import *


class Solution:
    """贪心. 为什么移动短的一边?
    贪心思想: 如果移动长的一边, 那么一定不可能产生更优解."""
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        res = 0
        while lo < hi:
            w = hi - lo
            if height[lo] <= height[hi]:
                s = w * height[lo]
                lo += 1
            else:
                s = w * height[hi]
                hi -= 1
            if s > res:
                res = s
        return res


class Solution2:
    "faster. python优化(max)"

    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        res = 0
        max_height = max(height)
        while lo < hi:
            w = hi - lo
            if height[lo] <= height[hi]:
                s = w * height[lo]
                lo += 1
            else:
                s = w * height[hi]
                hi -= 1
            if s > res:
                res = s
            if res >= w * max_height:
                break
        return res


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert Solution().maxArea(height) == 49
    assert Solution2().maxArea(height) == 49
