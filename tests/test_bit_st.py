from leetcode_alg import *
import unittest as ut


class TestBIT_ST(ut.TestCase):
    def test_bit2(self):
        bit2 = BinaryIndexedTree2([1, 2, 3, 4, 5])
        self.assertTrue(bit2.query_range(0, 4) == 15)
        bit2.update_range(0, 3, 1)
        self.assertTrue(bit2.query_range(0, 4) == 19)

    def test_st2(self):
        st2 = SegmentTree2([1, 2, 3, 4, 5])
        self.assertTrue(st2.query_range(0, 4) == 15)
        st2.update_range(0, 3, 1)
        self.assertTrue(st2.query_range(0, 4) == 19)


if __name__ == "__main__":
    ut.main()
