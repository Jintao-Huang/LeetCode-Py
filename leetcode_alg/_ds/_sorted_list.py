# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *


class SimpleSortedList:
    """由于使用的python, 自己设计的BBST, RBT不一定有较好的性能"""

    def __init__(self, nums: List[int], need_sort: bool = True) -> None:
        self.ssl = nums
        if need_sort:
            self.ssl.sort()

    def add(self, val: int) -> None:
        insort_right(self.ssl, val)

    def pop(self, i: int = -1) -> int:
        return self.ssl.pop(i)

    def bisect_left(self, val: int) -> int:
        return bisect_left(self.ssl, val)

    def bisect_right(self, val: int) -> int:
        return bisect_right(self.ssl, val)

    def remove(self, val: int) -> None:
        """删除最后一个出现的(faster than 删除第一个出现的)"""
        idx = self.bisect_right(val) - 1
        assert self.ssl[idx] == val
        self.ssl.pop(idx)

    def __len__(self) -> int:
        return len(self.ssl)

    def __getitem__(self, idx: int) -> int:
        return self.ssl[idx]


class SimpleSortedList2:
    """新增的功能: keys"""

    def __init__(self, nums: List[int], keys: Callable[[int], int],
                 need_sort: bool = True) -> None:
        """nums: const"""
        # 若未知x为int, 则需(keys(x), i, x)
        self._keys = keys
        self.ssl = [(keys(x), x) for x in nums]
        if need_sort:
            self.ssl.sort()

    def add(self, val: int) -> None:
        insort_right(self.ssl, (self._keys(val), val))

    def pop(self, i: int = -1) -> int:
        return self.ssl.pop(i)[1]

    def bisect_left(self, val: int) -> int:
        return bisect_left(self.ssl, (self._keys(val), val))

    def bisect_right(self, val: int) -> int:
        return bisect_right(self.ssl, (self._keys(val), val))

    def remove(self, val: int) -> None:
        idx = self.bisect_right(val) - 1
        assert self.ssl[idx][1] == val
        self.ssl.pop(idx)

    def __len__(self) -> int:
        return len(self.ssl)

    def __getitem__(self, idx: int) -> int:
        return self.ssl[idx][1]
