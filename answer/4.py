from leetcode_alg import *


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        # n <= m
        lo, hi = -1, n-1
        n_left = (n + m) >> 1

        def cond(mid: int) -> bool:
            """
            nums1[0..mid], | nums1[mid+1..n-1]
            nums2[0..mid2], | nums2[mid2+1..m-1]
            如果是n+m为奇数, |右边多1个元素. 
            """
            mid2 = n_left - mid - 2
            if mid+1 >= n or mid2 < 0:
                return True
            else:
                return nums1[mid+1] > nums2[mid2]
        #
        mid = lower_bound(lo, hi, cond)
        mid2 = n_left - mid - 2
        # 分类讨论
        # mid_right: |右边2个元素的最小值
        # mid_left: |左边2个元素的最大值
        if mid+1 >= n:
            mid_right = nums2[mid2+1]
        elif mid2+1 >= m:
            mid_right = nums1[mid+1]
        else:
            mid_right = min(nums1[mid+1], nums2[mid2+1])
        #
        if (n+m) % 2 == 1:
            return mid_right
        #
        if mid < 0:
            mid_left = nums2[mid2]
        elif mid2 < 0:
            mid_left = nums1[mid]
        else:
            mid_left = max(nums1[mid], nums2[mid2])
        return (mid_right + mid_left) / 2


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))

if __name__ == "__main__":
    nums1 = [2]
    nums2 = [1, 3]
    print(Solution().findMedianSortedArrays(nums1, nums2))
