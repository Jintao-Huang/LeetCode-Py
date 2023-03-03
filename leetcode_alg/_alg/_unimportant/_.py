from ..._types import *


def reverse(nums: Union[List[int], bytearray]) ->None:
    lo, hi = 0, len(nums)-1
    while lo<hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo += 1
        hi -= 1
