
from leetcode_alg import *

class Solution:
    def totalNQueens(self, n: int) -> int:
        res = n_queens(n)
        return len(res)


if __name__ == "__main__":
    n = 4
    assert Solution().totalNQueens(n) == 2
