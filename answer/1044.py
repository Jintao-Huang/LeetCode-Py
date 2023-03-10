
from leetcode_alg import *


class Solution:
    """recommended"""
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        sh = StringHasher(s)
        res_i = 0
        mod= int(1e18)+3
        def cond(mid: int) -> bool:
            # mid是长度.
            nonlocal res_i
            idx = sh.check(mid, mod)
            if res:=idx != -1:
                res_i = idx
            return res
        l = upper_bound(0, n-1, cond)
        return s[res_i:res_i+l]


if __name__ == "__main__":
    s = "aa"
    res = []
    print(Solution().longestDupSubstring(s))

    #
    # N = 1e9
    # for i in range(int(N), 2*INF):
    #     if is_prime(i):
    #         res.append(i)
    #     if len(res) == 5:
    #         break
    # print(res)
