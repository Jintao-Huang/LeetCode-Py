# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *
from .._alg._array import unique, diff


class _BITBase:
    """update_func=add"""
    @staticmethod
    def lowbit(idx: int) -> int:
        return idx & -idx

    @classmethod
    def _build_tree(cls, tree: List[int]) -> None:
        # 也可以通过先计算prefix_sum辅助数组, 使复杂度为O(n)
        n = len(tree)
        for i in range(1, n):
            p = i + cls.lowbit(i)
            if p < n:
                tree[p] += tree[i]

    @classmethod
    def _prefix_sum(cls, tree: List[int], hi: int) -> int:
        """sum(nums[1..hi+1])"""
        res = 0
        while hi >= 1:
            res += tree[hi]
            hi -= cls.lowbit(hi)
        return res

    @classmethod
    def _add(cls, tree: List[int], idx: int, val: int) -> None:
        n = len(tree)
        while idx < n:
            tree[idx] += val
            idx += cls.lowbit(idx)


class BinaryIndexedTree(_BITBase):
    def __init__(self, nums: List[int], build_tree: bool = True) -> None:
        """nums: const
        build_tree: 如果已知nums是全0数组(这很常见), 可以令build_tree=False
        """
        self.nums_len = len(nums)
        self.tree = [0]
        self.tree += nums
        if build_tree:
            self._build_tree(self.tree)

    def prefix_sum(self, hi: int) -> int:
        assert 0 <= hi < self.nums_len
        return self._prefix_sum(self.tree, hi+1)

    def query_range(self, lo: int, hi: int) -> int:
        """sum(nums[lo..hi])"""
        assert 0 <= lo <= hi < self.nums_len
        res = self._prefix_sum(self.tree, hi+1)
        if lo > 0:
            res -= self._prefix_sum(self.tree, lo)
        return res

    def add(self, idx: int, val: int) -> None:
        assert 0 <= idx < self.nums_len
        self._add(self.tree, idx+1, val)


def discretize(nums: List[int]) -> Dict[int, int]:
    """nums: const"""
    nums = sorted(nums)
    unique(nums)
    return {x: i for i, x in enumerate(nums)}


class BinaryIndexedTree2(_BITBase):
    """ref: https://books.halfrost.com/leetcode/ChapterThree/Binary_Indexed_Tree/
            https://oi-wiki.org/ds/fenwick/#%E5%8C%BA%E9%97%B4%E5%8A%A0%E5%8C%BA%E9%97%B4%E5%92%8C
    新增功能: update_range"""

    def __init__(self, nums: List[int], build_tree: bool = True) -> None:
        """
        build_tree: 如果nums数组全0, 则可以令build_tree=False
        """
        self.nums_len = len(nums)
        self.tree_C = diff(nums, 0)
        self.tree_D = [i * x for i, x in enumerate(self.tree_C)]
        if build_tree:
            self._build_tree(self.tree_C)
            self._build_tree(self.tree_D)

    def _prefix_sum(self, hi: int) -> int:
        res_Cn = super()._prefix_sum(self.tree_C, hi)
        res_Dn = super()._prefix_sum(self.tree_D, hi)
        return (hi + 1) * res_Cn - res_Dn

    def prefix_sum(self, hi: int) -> int:
        """sum(nums[..hi])"""
        assert 0 <= hi < self.nums_len
        return self._prefix_sum(hi+1)

    def query_range(self, lo: int, hi: int) -> int:
        """sum(nums[lo..hi])"""
        res = self._prefix_sum(hi+1)
        if lo > 0:
            res -= self._prefix_sum(lo)
        return res

    def _add(self, idx: int, val: int) -> None:
        super()._add(self.tree_C, idx, val)
        super()._add(self.tree_D, idx, idx*val)

    def update_range(self, lo: int, hi: int, val: int) -> None:
        assert 0 <= lo <= hi < self.nums_len
        self._add(lo+1, val)
        self._add(hi+2, -val)
