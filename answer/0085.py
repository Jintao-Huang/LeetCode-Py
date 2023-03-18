from leetcode_alg import *


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        hs = [0] * len(matrix[0])
        res = 0
        for vector in matrix:
            for j, c in enumerate(vector):
                if c == "1":
                    hs[j] += 1
                else:
                    hs[j] = 0
            lr = largest_rect(hs)
            if lr > res:
                res = lr
        return res


class Solution2:
    """单调栈"""
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        hs = [0] * len(matrix[0])
        res = 0
        for vector in matrix:
            for j, c in enumerate(vector):
                if c == "1":
                    hs[j] += 1
                else:
                    hs[j] = 0
            lr = largest_rect2(hs)
            if lr > res:
                res = lr
        return res

if __name__ == "__main__":
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    assert Solution().maximalRectangle(matrix) == 6
    assert Solution2().maximalRectangle(matrix) == 6
