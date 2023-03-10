# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *


class StringHasher:
    def __init__(self, s: str, min_char: int = ord("a"), base: int = 26) -> None:
        n = len(s)
        self.base = base
        self.ba = bytearray(n)
        min_char -= 1
        for i in range(n):
            self.ba[i] = ord(s[i])-min_char

    def check(self, length: int, mod: int = int(1e9)+7) -> int:
        """检查长度为length时, 是否有相等的子串"""
        dp = 0
        p = pow(self.base, length-1, mod)  # pow
        for c in self.ba[:length]:
            dp = (dp * self.base+c) % mod
        visited = {dp}
        for l, cl in enumerate(self.ba[:-length]):
            cr = self.ba[l+length]
            dp = ((dp-p*cl)* self.base+cr) % mod
            if dp in visited:
                return l+1
            visited.add(dp)
        return -1

