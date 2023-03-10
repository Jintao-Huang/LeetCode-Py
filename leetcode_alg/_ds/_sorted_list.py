# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *
# 数据量大时, 请使用sortedcontainers.SortedList, 更快

_T = TypeVar("_T")


class SimpleSortedList(Generic[_T]):
    """由于使用的python, 自己设计的BBST, RBT不一定有较好的性能"""

    def __init__(self, nums: Optional[List[_T]] = None,
                 key: Optional[Callable[[_T], _T]] = None, need_sort: bool = True) -> None:
        """nums: not const"""
        assert key is None
        if nums is None:
            nums = []
        self.ssl = nums
        if len(nums) > 1 and need_sort:
            self.ssl.sort()

    def __new__(cls, nums=None, key=None, need_sort=True) -> Union["SimpleSortedList[_T]", "_SimpleSortedListWithKey[_T]"]:
        if key is None:
            obj = object.__new__(cls)
        else:
            obj = object.__new__(_SimpleSortedListWithKey)
        return obj

    def add(self, val: _T) -> None:
        insort_right(self.ssl, val)

    def pop(self, i: int = -1) -> _T:
        return self.ssl.pop(i)

    def bisect_left(self, val: _T) -> int:
        return bisect_left(self.ssl, val)

    def bisect_right(self, val: _T) -> int:
        return bisect_right(self.ssl, val)

    def remove(self, val: _T) -> None:
        """删除最后一个出现的(faster than 删除第一个出现的)"""
        idx = bisect_right(self.ssl, val) - 1
        assert self.ssl[idx] == val
        self.ssl.pop(idx)



class _SimpleSortedListWithKey(SimpleSortedList[_T]):
    """新增的功能: key"""

    def __init__(self, nums: Optional[List[_T]] = None, key: Optional[Callable[[_T], _T]] = None,
                 need_sort: bool = True) -> None:
        """nums: not const"""
        assert key is not None
        if nums is None:
            nums = []
        self.key = key
        self.ssl = nums
        if len(nums) > 1 and need_sort:
            self.ssl.sort(key=key)
        self._keys = [key(x) for x in nums]

    def add(self, val: _T) -> None:
        k = self.key(val)
        idx = bisect_right(self._keys, k)
        self.ssl.insert(idx, val)
        self._keys.insert(idx, k)

    def pop(self, i: int = -1) -> _T:
        res = self.ssl.pop(i)
        self._keys.pop(i)
        return res

    def bisect_left(self, val: _T) -> int:
        return bisect_left(self._keys, self.key(val))

    def bisect_right(self, val: _T) -> int:
        return bisect_right(self._keys, self.key(val))

    def remove(self, val: _T) -> None:
        k = self.key(val)
        idx = bisect_right(self._keys, k) - 1
        assert self._keys[idx] == k
        self.ssl.pop(idx)
        self._keys.pop(idx)
