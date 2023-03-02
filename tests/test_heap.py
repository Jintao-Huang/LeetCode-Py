from leetcode_alg import *
import unittest as ut


class TestHeap2(ut.TestCase):
    def test_heap2(self):
        mpq = Heap2([])
        mpq.push((1, 5))
        mpq.push((2, 4))
        mpq.push((3, 4))
        mpq.push((4, 6))
        mpq.push((5, 1))
        self.assertTrue(mpq._id2pos == {1: 4, 2: 1, 3: 2, 4: 3, 5: 0})
        self.assertTrue(mpq.heap == [(5, 1), (2, 4), (3, 4), (4, 6), (1, 5)])
        self.assertTrue(mpq.pop() == (5, 1))
        self.assertTrue(mpq._id2pos == {1: 1, 2: 0, 3: 2, 4: 3})
        self.assertTrue(mpq.heap == [(2, 4), (1, 5), (3, 4), (4, 6)])
        mpq.push((1, 0))
        self.assertTrue(mpq._id2pos == {1: 0, 2: 1, 3: 2, 4: 3})
        self.assertTrue(mpq.heap == [(1, 0), (2, 4), (3, 4), (4, 6)])
        mpq.push((1, 5))
        self.assertTrue(mpq._id2pos == {1: 1, 2: 0, 3: 2, 4: 3})
        self.assertTrue(mpq.heap == [(2, 4), (1, 5), (3, 4), (4, 6)])


if __name__ == "__main__":
    ut.main()
