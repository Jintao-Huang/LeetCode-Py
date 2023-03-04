from leetcode_alg import *
import unittest as ut


class TestHeap(ut.TestCase):
    def test_heap2(self):
        mpq = Heap2()
        mpq.push((5, 1))
        mpq.push((4, 2))
        mpq.push((4, 3))
        mpq.push((6, 4))
        mpq.push((1, 5))
        self.assertTrue(mpq._id2pos == {1: 4, 2: 1, 3: 2, 4: 3, 5: 0})
        self.assertTrue(mpq.heap == [(1, 5), (4, 2), (4, 3), (6, 4), (5, 1)])
        self.assertTrue(mpq.pop() == (1, 5))
        self.assertTrue(mpq._id2pos == {1: 1, 2: 0, 3: 2, 4: 3})
        self.assertTrue(mpq.heap == [(4, 2), (5, 1), (4, 3), (6, 4)])
        mpq.push((0, 1))
        self.assertTrue(mpq._id2pos == {1: 0, 2: 1, 3: 2, 4: 3})
        self.assertTrue(mpq.heap == [(0, 1), (4, 2), (4, 3), (6, 4)])
        mpq.push((5, 1))
        self.assertTrue(mpq._id2pos == {1: 1, 2: 0, 3: 2, 4: 3})
        self.assertTrue(mpq.heap == [(4, 2), (5, 1), (4, 3), (6, 4)])


if __name__ == "__main__":
    ut.main()
