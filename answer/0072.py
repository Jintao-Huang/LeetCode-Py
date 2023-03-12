from leetcode_alg import *


class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        return edit_distance(s1, s2)


class Solution2:
    """recommended"""

    def minDistance(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)

        @cache
        def dfs(i: int, j: int) -> int:
            if i == 0:
                return j
            if j == 0:
                return i
            im, jm = i-1, j-1  # minus
            if s1[im] == s2[jm]:
                return dfs(im, jm)
            #
            return min(dfs(im, j), dfs(im, jm), dfs(i, jm))+1
        return dfs(n, m)


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    assert Solution().minDistance(word1, word2) == 3
    assert Solution2().minDistance(word1, word2) == 3
