
from leetcode_alg import *


class Solution:
    """recommended"""

    def strStr(self, haystack: str, needle: str) -> int:
        return kmp(haystack, needle)


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    haystack = "mississippi"
    needle = "issip"
    print(Solution().strStr(haystack, needle))
    print(Solution2().strStr(haystack, needle))
