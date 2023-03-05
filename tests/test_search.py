from leetcode_alg import *
import unittest as ut

class TestSearch(ut.TestCase):
    def test_bs(self):
        nums = [2, 2, 2]
        res = []
        res.append(lower_bound(0, 3, lambda i: nums[i] >= 2))
        res.append(lower_bound(0, 3, lambda i: nums[i] > 2))
        res.append(upper_bound(-1, 2, lambda i: nums[i] < 2))
        res.append(lower_bound(-1, 2, lambda i: nums[i] <=2))
        self.assertTrue(res, [0, 3, -1, 2])

    def test_n_queens(self):
        self.assertTrue(n_queens(4) == [[1, 3, 0, 2], [2, 0, 3, 1]])

if __name__ == "__main__":
    ut.main()