from leetcode_alg._alg._unimportant import *
import unittest as ut


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

if __name__ == "__main__":
    ut.main()
