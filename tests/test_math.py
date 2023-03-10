from leetcode_alg.ext import *
import unittest as ut


class TestMath(ut.TestCase):
    def test_fast_pow(self):
        # ref: https://leetcode.cn/problems/super-pow/
        x = fast_pow(2147483647, 200, 1337)
        y = pow(2147483647, 200, 1337)
        self.assertTrue(x == y)


if __name__ == "__main__":
    ut.main()
