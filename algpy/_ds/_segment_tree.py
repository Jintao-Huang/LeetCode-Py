from typing import List, Union, Callable
import math
from operator import add


class SegmentTree:
    def _cal_tree_len(self, nums_len: int) -> int:
        """
        nums_len: len(nums), 或指树的最底层必须满足的数量. 
        return: 你也可以直接返回4*nums_len(这足够用, 也足够简单)
        """
        h = math.ceil(math.log2(nums_len) + 1)  # 树高
        tree_len = (1 << h) - 1  # 满
        return tree_len

    def __init__(self, nums: List[int], build_tree: bool = True,
                 update_func: Callable[[int, int], int] = add,
                 merge_func: Callable[[int, int], int] = add) -> None:
        """
        build_tree: 如果已知nums是全0数组(这很常见), 可以令build_tree=False
        update_func: func(origin, value) -> new
            e.g. replace: lambda x, y: y
                 add: add. (default)
        merge_func: func(区间1, 区间2) -> 总区间
            e.g. sum: add. (default)
                 max, min
        """
        self._update_func = update_func
        self._merge_func = merge_func
        #
        self.nums_len = len(nums)
        tree_len = self._cal_tree_len(self.nums_len)
        self.tree = [0] * tree_len  # 堆结构
        if build_tree:
            self._build_tree(nums, 0, 0, self.nums_len - 1)

    def _build_tree(self, nums: List[int], tree_idx: int, lo: int, hi: int) -> None:
        """[lo..hi]: nums的idx"""
        if lo == hi:
            self.tree[tree_idx] = nums[lo]
            return
        #
        mid, lc = (lo + hi) // 2, (tree_idx << 1) + 1
        self._build_tree(nums, lc, lo, mid)
        self._build_tree(nums, lc+1, mid+1, hi)
        self.tree[tree_idx] = self._merge_func(self.tree[lc], self.tree[lc+1])

    def _query_range(self, tree_idx: int, lo: int, hi: int, q_lo: int, q_hi: int) -> int:
        """[lo..hi], [q_lo..q_hi]"""
        if lo == q_lo and hi == q_hi:
            return self.tree[tree_idx]
        #
        # 分类讨论: q在lc[lo..mid], q在rc[mid+1..hi], q两边都有
        mid, lc = (lo + hi) // 2, (tree_idx << 1) + 1
        if q_hi <= mid:
            return self._query_range(lc, lo, mid, q_lo, q_hi)
        elif q_lo >= mid + 1:
            return self._query_range(lc+1, mid+1, hi, q_lo, q_hi)
        else:
            return self._merge_func(
                self._query_range(lc, lo, mid, q_lo, mid),
                self._query_range(lc+1, mid+1, hi, mid+1, q_hi)
            )

    def query_range(self, q_lo: int, q_hi: int) -> int:
        """[q_lo..q_hi]"""
        assert 0 <= q_lo <= q_hi < self.nums_len
        return self._query_range(0, 0, self.nums_len - 1, q_lo, q_hi)

    def _update(self, tree_idx: int, lo: int, hi: int, u_idx: int, u_val: int) -> None:
        # 可以改成迭代版本
        if lo == hi:
            self.tree[tree_idx] = self._update_func(self.tree[tree_idx], u_val)
            return
        mid, lc = (lo + hi) // 2, (tree_idx << 1) + 1
        if u_idx <= mid:
            self._update(lc, lo, mid, u_idx, u_val)
        else:
            self._update(lc+1, mid+1, hi, u_idx, u_val)
        self.tree[tree_idx] = self._merge_func(self.tree[lc], self.tree[lc+1])

    def update(self, idx: int, val: int) -> None:
        assert 0 <= idx < self.nums_len
        self._update(0, 0, self.nums_len-1, idx, val)
