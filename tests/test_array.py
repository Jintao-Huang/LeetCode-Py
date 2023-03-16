from leetcode_alg import *
import unittest as ut
import numpy as np
import mini_lightning as ml


class TestArray(ut.TestCase):
    partition([5, 0, 2, 1, 4, 3, 6, 8, 9, 7], 0, 5)

    def test_partition(self):
        x = [5, 3, 6, 1, 2, 5, 7, 3, 4, 6]
        self.assertTrue(partition(x, 0, len(x) - 1) == 5)
        self.assertTrue(x == [3, 1, 2, 3, 4, 5, 7, 6, 6, 5])
        x = [5, 0, 2, 1, 4, 3, 6, 8, 9, 7]
        self.assertTrue(partition(x, 0, 5) == 5)
        #
        x = [1, 4, 3, 2, 0]
        self.assertTrue(partition(x, 0, 4) == 1)
        self.assertTrue(x == [0, 1, 3, 2, 4])
        #
        x = [5, 3, 6, 1, 2, 5, 7, 3, 4, 6]
        self.assertTrue(partition2(x, 0, len(x) - 1) == 6)
        self.assertTrue(x == [4, 3, 3, 1, 2, 5, 5, 7, 6, 6])
        #
        x = [1, 4, 3, 2, 0]
        self.assertTrue(partition2(x, 0, 4) == 1)
        self.assertTrue(x == [0, 1, 3, 2, 4])
        #
        n = 100000
        print("partition")
        ml.test_time(lambda: partition(np.random.permutation(n).tolist(), 0, n-1), 10, 1)
        ml.test_time(lambda: partition2(np.random.permutation(n).tolist(), 0, n-1), 10, 1)

    def test_merge(self):
        x = [1, 2, 5, 7, 8, 0, 3, 4, 6, 9]
        sorted_x = sorted(x)
        y = x[:]
        merge(x, 0, 4, 9)
        self.assertTrue(x == sorted_x)
        merge2(y, 0, 4, 9)
        self.assertTrue(y == sorted_x)
        #
        n = 100000
        nums = np.arange(n).tolist() + np.arange(n).tolist()
        print("merge")
        ml.test_time(lambda: merge(nums[:], 0, n-1, 2*n-1), 10, 1)
        ml.test_time(lambda: list(merge_heapq(nums[:n], nums[n+1:])), 10, 1)
        ml.test_time(lambda: merge2(nums[:], 0, n-1, 2*n-1), 10, 1)
        #
        nums = np.arange(2*n).tolist()
        ml.test_time(lambda: merge(nums[:], 0, n-1, 2*n-1), 10, 1)
        ml.test_time(lambda: merge2(nums[:], 0, n-1, 2*n-1), 10, 1)
        #
        nums = np.arange(n, 2 * n).tolist() + np.arange(n//2, n+n//2).tolist()
        ml.test_time(lambda: merge(nums[:], 0, n-1, 2*n-1), 10, 1)
        ml.test_time(lambda: merge2(nums[:], 0, n-1, 2*n-1), 10, 1)

    def test_quick_select(self):
        x = np.random.permutation(10).tolist()
        a = randint(0, 9)
        self.assertTrue(quick_select(x, a) == a)


if __name__ == "__main__":
    ut.main()
