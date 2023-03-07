from leetcode_alg import *
import unittest as ut


class TestMath(ut.TestCase):
    def test_fast_pow(self):
        # ref: https://leetcode.cn/problems/super-pow/
        x = fast_pow(2147483647, 200, 1337)
        self.assertTrue(x == 1198)


if __name__ == "__main__":
    ut.main()
