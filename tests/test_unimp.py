from leetcode_alg.ext import *
import unittest as ut
import numpy as np
import mini_lightning as ml
import math


class TestUnimp(ut.TestCase):
    def test_bs(self):
        x = [1, 2, 2, 2, 3]
        self.assertTrue(bisect_left(x, 2), 1)
        self.assertTrue(bisect_right(x, 2), 4)
        self.assertTrue(binary_search(x, 4), -1)
        self.assertTrue(binary_search(x, 2), 2)
        self.assertTrue(binary_search(x, 0), -1)

    def test_merge_sort(self):
        nums = [1, 4, 6, 3, 2, 5, 0, 8, 9, 7]
        merge_sort(nums, 0, len(nums)-1)
        self.assertTrue(nums == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_quick_sort(self):
        nums = [1, 4, 6, 3, 2, 5, 0, 8, 9, 7]
        quick_sort(nums, 0, len(nums)-1)
        self.assertTrue(nums == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_prefix_sum(self):
        nums = [1, 2, 3, 4, 5, 6]
        res = list(accumulate(nums))
        res2 = prefix_sum(nums)
        self.assertTrue(res == res2)
        res = list(accumulate(nums, initial=1))
        res2 = prefix_sum(nums, initial=1)
        self.assertTrue(res == res2)
        n = 10000
        x = np.random.permutation(n).tolist()
        print("prefix_sum")
        y2 = ml.test_time(lambda: prefix_sum(x, 1), 10)
        y = ml.test_time(lambda: list(accumulate(x, initial=1)), 10)
        self.assertTrue(y == y2)

    def test_heap_sort(self):
        nums = [1, 4, 6, 3, 2, 5, 0, 8, 9, 7]
        heap_sort(nums)
        self.assertTrue(nums == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        nums = [1, 4, 6, 3, 2, 5, 0, 8, 9, 7]
        res = heap_sort2(nums)
        self.assertTrue(res == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertTrue(nums == [])
        heap_sort([])
        heap_sort2([])

    def test_gcd_lcm(self):
        x, y = 20, 25

        self.assertTrue(gcd(x, y) == math.gcd(x, y))
        self.assertTrue(lcm(x, y) == math.lcm(x, y))


if __name__ == "__main__":
    ut.main()
