
from leetcode_alg import *


class Solution:
    """recommended"""
    def largestRectangleArea(self, heights: List[int]) -> int:
        return largest_rect(heights)


class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return largest_rect2(heights)


if __name__ == "__main__":
    heights = [2, 1, 2]
    assert Solution().largestRectangleArea(heights) == 3
    assert Solution2().largestRectangleArea(heights) == 3
