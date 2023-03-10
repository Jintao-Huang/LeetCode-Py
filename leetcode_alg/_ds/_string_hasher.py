# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *


class StringHasher:
    def __init__(self, s: str, min_char: int = ord("a"), base: int = 26, mod: int = int(1e18)+3) -> None:
        """在c++中, 由于long long越界问题, 可以使用双mod处理. e.g. int(1e9)+7, int(1e9)+9
        或哈希相等后, 依旧选择字符串中几个字符进行比较"""
        self.n = len(s)
        self.mod = mod
        min_char -= 1
        ba = bytearray(self.n)
        for i in range(self.n):
            ba[i] = ord(s[i])-min_char
        self.ps = list(accumulate(ba, lambda x, y: (x * base + y) % mod))
        self.base = list(accumulate(range(self.n - 1), lambda b, _: ((b * base) % mod), initial=1))

    def get_hash(self, lo: int, hi: int) -> int:
        """[lo..hi]"""
        res = self.ps[hi]
        if lo > 0:
            res -= self.ps[lo-1]*self.base[hi-lo+1]
        return res % self.mod
