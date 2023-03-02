from algpy import *


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.st = SegmentTree(nums, True, lambda x, y: y)

    def update(self, index: int, val: int) -> None:
        self.st.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.query_range(left, right)


if __name__ == "__main__":
    res = call_callable_list(
        ["NumArray", "update", "update", "update", "sumRange", "update",
            "sumRange", "update", "sumRange", "sumRange", "update"],
        [[[7, 2, 7, 2, 0]], [4, 6], [0, 2], [0, 9], [4, 4], [3, 8], [0, 4], [4, 1], [0, 3], [0, 4], [0, 4]],
        globals())
    print(res)


#

class NumArray2:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = BinaryIndexedTree(nums, True)

    def update(self, index: int, val: int) -> None:
        diff_val = val-self.nums[index]
        self.nums[index] = val
        self.bit.update(index, diff_val)

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.query_range(left, right)


if __name__ == "__main__":
    res = call_callable_list(
        ["NumArray2", "update", "update", "update", "sumRange", "update",
            "sumRange", "update", "sumRange", "sumRange", "update"],
        [[[7, 2, 7, 2, 0]], [4, 6], [0, 2], [0, 9], [4, 4], [3, 8], [0, 4], [4, 1], [0, 3], [0, 4], [0, 4]],
        globals())
    print(res)
