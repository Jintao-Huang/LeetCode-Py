
from leetcode_alg import *


class StringHasher2:
    """优化"""

    def __init__(self, s: str, min_char: int = ord("a"), base: int = 26) -> None:
        n = len(s)
        self.s = s
        self.base = base
        self.ba = bytearray(n)
        min_char -= 1
        for i in range(n):
            self.ba[i] = ord(s[i])-min_char

    def check(self, length: int, mod: int = int(1e18)+3) -> int:
        """检查长度为length时, 是否有相等的子串"""
        dp = 0  # hash
        p = pow(self.base, length-1, mod)  # pow
        for i in range(length):
            c = self.ba[i]
            dp = (dp * self.base+c) % mod
        visited = {dp}
        n = len(self.ba)
        for lo in range(n-length):
            cl = self.ba[lo]
            cr = self.ba[lo+length]
            dp = ((dp-p*cl) * self.base+cr) % mod
            if dp in visited:
                return lo+1
            visited.add(dp)
        return -1


class Solution:
    """faster"""

    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        sh = StringHasher2(s)
        res_i = 0
        mod = int(1e18)+3

        def cond(mid: int) -> bool:
            # mid是长度.
            nonlocal res_i
            idx = sh.check(mid, mod)
            if res := idx != -1:
                res_i = idx
            return res
        l = upper_bound(0, n-1, cond)
        return s[res_i:res_i+l]


class Solution2:
    """使用template"""

    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        mod = int(1e18)+3
        sh = StringHasher(s, mod=mod)
        res_i = 0

        def cond(mid: int) -> bool:
            # mid是长度.
            nonlocal res_i
            visited = set()
            for lo in range(n-mid + 1):
                h = sh.get_hash(lo, lo+mid-1)
                if h in visited:
                    res_i = lo
                    return True
                visited.add(h)
            return False
        l = upper_bound(0, n-1, cond)
        return s[res_i:res_i+l]


class Solution3:
    """mod使用int(1e9)+7(避免C++的long long越界情况). 
    这里使用对部分字符串进行比较的方式降低错误率. 你也可以通过双哈希的方式处理. 
    当然速度很慢. 
    note: 哈希碰撞的概率比直觉上高得多, ref: 生日悖论"""

    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        mod = int(1e9)+7
        sh = StringHasher(s, mod=mod)
        res_i = 0

        def cond(mid: int) -> bool:
            # mid是长度.
            nonlocal res_i
            visited = DefaultDict[int, Set[str]](set)
            for lo in range(n-mid + 1):
                hi = lo+mid-1
                h = sh.get_hash(lo, hi)
                example_s = s[lo:min(lo+2, hi)]
                if h in visited and example_s in visited[h]:
                    res_i = lo
                    return True
                visited[h].add(example_s)
            return False
        l = upper_bound(0, n-1, cond)
        return s[res_i:res_i+l]


if __name__ == "__main__":
    res = []
    s = "zxcvdqkfawuytt"
    assert Solution().longestDupSubstring(s) == "t"
    assert Solution2().longestDupSubstring(s) == "t"
    assert Solution3().longestDupSubstring(s) == "t"

#

# if __name__ == "__main__":
#     s = int(1e9)
#     res = []
#     for x in range(s, s+100):
#         if is_prime(x):
#             res.append(x)
#     print(res)
