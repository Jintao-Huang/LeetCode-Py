from typing import List, Callable, Literal


class BinaryIndexedTree:
    def __init__(self, nums: List[int], build_tree: bool = True) -> None:
        """
        build_tree: 如果已知nums是全0数组(这很常见), 可以令build_tree=False
        """
        self.nums = nums
        self.nums_len = len(nums)
        self.tree = self.nums.copy()
        if build_tree:
            self._build_tree(nums)

    @staticmethod
    def _lowbit(idx: int) -> int:
        return idx & -idx

    def _build_tree(self, nums: List[int]) -> None:
        for i in range(self.nums_len):
            p = i + self._lowbit(i+1)
            if p < self.nums_len:
                self.tree[p] += self.tree[i]

    def _prefix_sum(self, hi: int) -> int:
        """sum(nums[..hi])"""
        res = 0
        while hi >= 0:
            res += self.tree[hi]
            hi -= self._lowbit(hi+1)
        return res

    def query_range(self, lo: int, hi: int) -> int:
        """sum(nums[lo..hi])"""
        assert 0 <= lo <= hi < self.nums_len
        res = self._prefix_sum(hi)
        if lo > 0:
            res -= self._prefix_sum(lo - 1)
        return res

    def update(self, idx: int, diff_val: int) -> None:
        """`add mode`"""
        assert 0 <= idx < self.nums_len
        while idx < self.nums_len:
            self.tree[idx] += diff_val
            idx += self._lowbit(idx+1)
