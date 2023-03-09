from leetcode_alg import *
import unittest as ut


class TestStr(ut.TestCase):
    def test_kmp(self):
        s = "aabaab"
        self.assertTrue(build_nextval(s) == [0, 1, 0, 0, 1, 3])


if __name__ == "__main__":
    ut.main()
