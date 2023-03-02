from typing import List, Literal, Optional
import math
from operator import add


_func_mapper = {
    "add": add,
    "replace": lambda x, y: y,
    "min": min,
    "max": max
}


class STBase:
    def __init__(self, nums: List[int], build_tree: bool = True,
                 update_func: Literal["add", "replace"] = "add",
                 merge_func: Literal["add", "min", "max"] = "add") -> None:
        """
        build_tree: 如果已知nums是全0数组(这很常见), 可以令build_tree=False
        update_func: func(origin, value) -> new
            e.g. replace: lambda x, y: y
                 add: add. (default)
        merge_func: func(区间1, 区间2) -> 总区间
            e.g. sum: add. (default)
                 max, min
        """
        self._update_func_s = update_func
        self._merge_func_s = merge_func
        self._update_func = _func_mapper[update_func]
        self._merge_func = _func_mapper[merge_func]
        #
        self.nums_len = len(nums)
        tree_len = 0
        if self.nums_len > 0:
            h = self._cal_tree_height(self.nums_len)
            tree_len = (1 << h) - 1
        self.tree = [0] * tree_len  # 堆结构
        if build_tree:
            self._build_tree(nums, 0, 0, self.nums_len - 1)

    def _cal_tree_height(self, nums_len: int) -> int:
        return math.ceil(math.log2(nums_len) + 1)

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

    def query_range(self, q_lo: int, q_hi: int) -> int:
        """[q_lo..q_hi]"""
        assert 0 <= q_lo <= q_hi < self.nums_len
        return self._query_range(0, 0, self.nums_len - 1, q_lo, q_hi)


class SegmentTree(STBase):
    def _query_range(self, tree_idx: int, lo: int, hi: int, q_lo: int, q_hi: int) -> int:
        """[lo..hi], [q_lo..q_hi]"""
        if lo == q_lo and hi == q_hi:
            return self.tree[tree_idx]
        # 分类讨论
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


class SegmentTree2(STBase):
    """ref: https://oi-wiki.org/ds/seg/#%E7%BA%BF%E6%AE%B5%E6%A0%91%E7%9A%84%E5%8C%BA%E9%97%B4%E4%BF%AE%E6%94%B9%E4%B8%8E%E6%87%92%E6%83%B0%E6%A0%87%E8%AE%B0
    新增功能: update_range"""

    def __init__(self, nums: List[int], build_tree: bool = True,
                 update_func: Literal["add", "replace"] = "add",
                 merge_func: Literal["add", "min", "max"] = "add",
                 lazyt_init_val: Optional[int] = None) -> None:
        super().__init__(nums, build_tree, update_func, merge_func)
        self._lazyt_init_val = lazyt_init_val
        #
        lazyt_len = 0
        if self.nums_len > 0:
            h = self._cal_tree_height(self.nums_len)
            lazyt_len = (1 << (h-1)) - 1
        # lazy_tag[i]: tree[i]已更新, tree[lc], tree[lc+1]未更新.
        #   if update_func is add, 你可以使用0作为lazyt_init_val
        self.lazy_tag = [lazyt_init_val] * lazyt_len

    def _update_lazy_tag(self, tree_idx: int, lo: int, hi: int) -> None:
        mid, lc = (lo + hi) // 2, (tree_idx << 1) + 1
        lazyt = self.lazy_tag[tree_idx]
        #
        if lazyt != self._lazyt_init_val:
            assert lazyt is not None
            if self._merge_func_s == "add":
                self.tree[lc] = self._update_func(self.tree[lc], lazyt * (mid-lo+1))
                self.tree[lc+1] = self._update_func(self.tree[lc+1], lazyt * (hi-mid))
            else:  # min/max
                self.tree[lc] = self._update_func(self.tree[lc], lazyt)
                self.tree[lc+1] = self._update_func(self.tree[lc+1], lazyt)
            self.lazy_tag[tree_idx] = self._lazyt_init_val
            if lc < len(self.lazy_tag):
                self.lazy_tag[lc] = lazyt
                self.lazy_tag[lc+1] = lazyt

    def _query_range(self, tree_idx: int, lo: int, hi: int, q_lo: int, q_hi: int) -> int:
        """[lo..hi], [q_lo..q_hi]"""
        if lo == q_lo and hi == q_hi:
            return self.tree[tree_idx]
        self._update_lazy_tag(tree_idx, lo, hi)
        # 分类讨论
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

    def _update_range(self, tree_idx: int, lo: int, hi: int, u_lo: int, u_hi: int, u_val: int) -> None:
        """[lo..hi], [u_lo..u_hi]"""
        if lo == u_lo and hi == u_hi:
            if self._merge_func_s == "add":
                self.tree[tree_idx] = self._update_func(self.tree[tree_idx], u_val*(hi-lo+1))
            else:
                self.tree[tree_idx] = self._update_func(self.tree[tree_idx], u_val)
            if tree_idx < len(self.lazy_tag):
                self.lazy_tag[tree_idx] = u_val
            return
        # 分类讨论
        self._update_lazy_tag(tree_idx, lo, hi)
        mid, lc = (lo + hi) // 2, (tree_idx << 1) + 1
        if u_hi <= mid:
            self._update_range(lc, lo, mid, u_lo, u_hi, u_val)
        elif u_lo >= mid+1:
            self._update_range(lc+1, mid+1, hi, u_lo, u_hi, u_val)
        else:
            self._update_range(lc, lo, mid, u_lo, mid, u_val)
            self._update_range(lc+1, mid+1, hi, mid+1, u_hi, u_val)
        self.tree[tree_idx] = self._merge_func(self.tree[lc], self.tree[lc+1])

    def update_range(self, lo: int, hi: int, val: int) -> None:
        """[lo..hi]"""
        assert 0 <= lo <= hi < self.nums_len
        self._update_range(0, 0, self.nums_len-1, lo, hi, val)
