from leetcode_alg import *


class Solution:
    """recommended"""

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        # n <= m
        n_left = (n + m) >> 1

        def cond(i: int) -> bool:
            """
            nums1[0..i], | nums1[i+1..n-1]
            nums2[0..i2], | nums2[i2+1..m-1]
            如果是n+m为奇数, |右边多1个元素. 
            """
            i2 = n_left - i - 2
            if i+1 >= n or i2 < 0:
                return True
            else:
                return nums1[i+1] > nums2[i2]
        #
        i = lower_bound(-1, n-1, cond)
        i2 = n_left - i - 2
        # 分类讨论
        # mid_right: |右边2个元素的最小值
        # mid_left: |左边2个元素的最大值
        if i+1 >= n:
            mid_right = nums2[i2+1]
        elif i2+1 >= m:
            mid_right = nums1[i+1]
        else:
            mid_right = min(nums1[i+1], nums2[i2+1])
        #
        if (n+m) % 2 == 1:
            return mid_right
        #
        if i < 0:
            mid_left = nums2[i2]
        elif i2 < 0:
            mid_left = nums1[i]
        else:
            mid_left = max(nums1[i], nums2[i2])
        return (mid_right + mid_left) / 2


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        n = len(nums1)
        mid = n >> 1
        if n % 2 == 0:
            return (nums1[mid-1]+nums1[mid])/2
        else:
            return nums1[mid]


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 2.5
    assert Solution2().findMedianSortedArrays(nums1, nums2) == 2.5

if __name__ == "__main__":
    nums1 = [2]
    nums2 = [1, 3]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 2
    assert Solution2().findMedianSortedArrays(nums1, nums2) == 2
