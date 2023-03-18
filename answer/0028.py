
from leetcode_alg import *


class Solution:
    """recommended"""

    def strStr(self, haystack: str, needle: str) -> int:
        return kmp(haystack, needle)


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


class Solution3:
    """字符串哈希"""
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        sh = StringHasher(needle, mod=int(1e9)+7)
        h = sh.get_hash(0, m-1)
        sh2 = StringHasher(haystack, mod=int(1e9)+7)
        for lo in range(n-m+1):
            hi = lo+m-1
            if sh2.get_hash(lo, hi) == h:
                return lo
        return -1


if __name__ == "__main__":
    haystack = "mississippi"
    needle = "issip"
    assert Solution().strStr(haystack, needle) == 4
    assert Solution2().strStr(haystack, needle) == 4
    assert Solution3().strStr(haystack, needle) == 4
