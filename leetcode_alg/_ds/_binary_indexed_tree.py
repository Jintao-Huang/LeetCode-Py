from typing import List, Dict


class BITBase:
    """update_func=add"""
    @staticmethod
    def lowbit(idx: int) -> int:
        return idx & -idx

    @classmethod
    def _build_tree(cls, tree: List[int]) -> None:
        # 也可以通过先计算prefix_sum辅助数组, 使复杂度为O(n)
        n = len(tree)
        for i in range(n):
            p = i + cls.lowbit(i+1)
            if p < n:
                tree[p] += tree[i]

    @classmethod
    def _prefix_sum(cls, tree: List[int], hi: int) -> int:
        """sum(nums[..hi])"""
        res = 0
        while hi >= 0:
            res += tree[hi]
            hi -= cls.lowbit(hi+1)
        return res

    @classmethod
    def _add(cls, tree: List[int], idx: int, val: int) -> None:
        n = len(tree)
        while idx < n:
            tree[idx] += val
            idx += cls.lowbit(idx+1)


class BinaryIndexedTree(BITBase):
    def __init__(self, nums: List[int], build_tree: bool = True) -> None:
        """
        build_tree: 如果已知nums是全0数组(这很常见), 可以令build_tree=False
        """
        self.tree = nums.copy()
        if build_tree:
            self._build_tree(self.tree)

    def prefix_sum(self, hi: int) -> int:
        assert 0 <= hi < len(self.tree)
        return self._prefix_sum(self.tree, hi)

    def query_range(self, lo: int, hi: int) -> int:
        """sum(nums[lo..hi])"""
        assert 0 <= lo <= hi < len(self.tree)
        res = self._prefix_sum(self.tree, hi)
        if lo > 0:
            res -= self._prefix_sum(self.tree, lo - 1)
        return res

    def add(self, idx: int, val: int) -> None:
        """update_func=add"""
        assert 0 <= idx < len(self.tree)
        self._add(self.tree, idx, val)


def discretize(nums: List[int]) -> Dict[int, int]:
    nums = sorted(nums)
    unique(nums)
    return {x: i for i, x in enumerate(nums)}


def unique(nums: List[int]) -> None:
    n = len(nums)
    lo = 1  # 将被赋值, 但未被赋值. ignore 0
    for hi in range(1, n):
        if nums[hi] != nums[hi-1]:
            nums[lo] = nums[hi]
            lo += 1
    #
    for _ in range(lo, n):
        nums.pop()


def diff(nums: List[int]) -> List[int]:
    """C0=A0, C1=A1-A0, ..."""
    if len(nums) == 0:
        return []
    res = [nums[0]]
    n = len(nums)
    for i in range(1, n):
        res.append(nums[i] - nums[i-1])
    return res


class BinaryIndexedTree2(BITBase):
    """ref: https://books.halfrost.com/leetcode/ChapterThree/Binary_Indexed_Tree/
            https://oi-wiki.org/ds/fenwick/#%E5%8C%BA%E9%97%B4%E5%8A%A0%E5%8C%BA%E9%97%B4%E5%92%8C
    新增功能: update_range"""

    def __init__(self, nums: List[int], build_tree: bool = True) -> None:
        """
        build_tree: 如果nums数组全0, 则可以令build_tree=False
        """
        self.nums = nums
        self.tree_C = diff(self.nums)
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
        assert 0 <= hi < len(self.tree_C)
        return self._prefix_sum(hi)

    def query_range(self, lo: int, hi: int) -> int:
        """sum(nums[lo..hi])"""
        res = self._prefix_sum(hi)
        if lo > 0:
            res -= self._prefix_sum(lo - 1)
        return res

    def _add(self, idx: int, val: int) -> None:
        super()._add(self.tree_C, idx, val)
        super()._add(self.tree_D, idx, idx*val)

    def update_range(self, lo: int, hi: int, val: int) -> None:
        assert 0 <= lo <= hi < len(self.tree_C)
        self._add(lo, val)
        self._add(hi+1, -val)
