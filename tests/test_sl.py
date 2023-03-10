from leetcode_alg import *
import unittest as ut


class TestSL(ut.TestCase):
    def test_sl_sl2(self):
        x = [1, 3, 3, 6, 7, 1]
        res = []
        for sl in [SimpleSortedList(x[:]), SimpleSortedList(x[:], neg)]:
            sl.add(0)
            sl.add(100)
            sl.remove(6)
            res.append(sl.bisect_left(3))
            res.append(sl.bisect_right(3))
            res.append(sl.pop())
            res.append(sl.ssl)
        self.assertTrue(
            res == [
                3, 5, 100, [0, 1, 1, 3, 3, 7],
                2, 4, 0, [100, 7, 3, 3, 1, 1]
            ]
        )


if __name__ == "__main__":
    ut.main()
