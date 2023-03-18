from leetcode_alg import *


class Solution:
    """recommended. LIS"""

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        if n > m:
            return self.longestCommonSubsequence(s2, s1)
        # n <= m
        if s1 in s2:
            return n
        return LCS(s1, s2)


class Solution2:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        if n > m:
            return self.longestCommonSubsequence(s2, s1)
        # n <= m
        if s1 in s2:
            return n
        #
        return LCS2(s1, s2)


if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    assert Solution().longestCommonSubsequence(text1, text2) == 3
    assert Solution2().longestCommonSubsequence(text1, text2) == 3
    print(LCS3(text1, text2))
