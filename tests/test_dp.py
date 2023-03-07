from leetcode_alg import *
import unittest as ut


class TestDP(ut.TestCase):
    def test_matrix_chain(self):
        nums = [30, 35, 15, 5, 10, 20, 25]
        self.assertTrue(matrix_chain(nums) == 15125)
        print(matrix_chain2(nums) == (15125, '((A0(A1A2))((A3A4)A5))'))


if __name__ == "__main__":
    ut.main()
