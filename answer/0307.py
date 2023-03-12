from leetcode_alg import *


class NumArray:
    """recommended"""

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = BinaryIndexedTree(nums, True)

    def update(self, index: int, val: int) -> None:
        diff_val = val-self.nums[index]
        self.nums[index] = val
        self.bit.add(index, diff_val)

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.query_range(left, right)


class NumArray2:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.st = SegmentTree(nums, True, "replace")

    def update(self, index: int, val: int) -> None:
        self.st.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.query_range(left, right)


if __name__ == "__main__":

    callable_list = ["NumArray", "update", "update", "update", "sumRange", "update",
            "sumRange", "update", "sumRange", "sumRange", "update"]
    args_list = [[[7, 2, 7, 2, 0]], [4, 6], [0, 2], [0, 9], [4, 4], [3, 8], [0, 4], [4, 1], [0, 3], [0, 4], [0, 4]]
    y = call_callable_list(callable_list, args_list, globals())
    callable_list[0] = "NumArray2"
    y2 = call_callable_list(callable_list, args_list, globals())
    assert y == [None, None, None, 6, None, 32, None, 26, 27, None]
    assert y2 == [None, None, None, 6, None, 32, None, 26, 27, None]

