from leetcode_alg import *


class Solution:
    """recommended"""

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        if n < m:
            return self.longestCommonSubsequence(s2, s1)
        if s2 in s1:
            return m
        #
        mapper = DefaultDict[str, List[int]](list)
        for i in reversed(range(n)):
            mapper[s1[i]].append(i)
        nums = []
        for c in s2:
            if c in mapper:
                nums.extend(mapper[c])
        return LIS(nums)


class Solution2:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        if n < m:
            return self.longestCommonSubsequence(s2, s1)
        if s2 in s1:
            return m
        #
        return LCS(s1, s2)


if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    assert Solution().longestCommonSubsequence(text1, text2) == 3
    assert Solution2().longestCommonSubsequence(text1, text2) == 3
    print(LCS2(text1, text2))
