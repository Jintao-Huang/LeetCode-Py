from leetcode_alg import *
from leetcode_alg.ext import combinations_, combinations2


class Solution:
    """faster"""

    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n+1), k))  # leetcode不检查list和tuple.


class Solution2:
    """回溯法"""

    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations2(list(range(1, n+1)), k)


class Solution3:
    """迭代法"""

    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations_(list(range(1, n+1)), k)


if __name__ == "__main__":
    assert Solution().combine(4, 2) == [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    assert Solution2().combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert Solution3().combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert Solution2().combine(0, 0) == [[]]
    assert Solution3().combine(0, 0) == [[]]
