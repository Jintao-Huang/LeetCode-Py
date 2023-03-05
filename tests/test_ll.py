from leetcode_alg import *
import unittest as ut


class TestLL(ut.TestCase):
    def test_ll(self):
        res = []
        l = LinkedList([1, 2, 3])
        l.append(4)
        l.pop_left()
        res.append(l.tolist())
        res.append(l[0].val)
        res.append(l[-1].val)
        res.append(len(l))
        l.clear()
        res.append(l.tolist())
        res.append(len(l))
        self.assertTrue(res == [
            [2, 3, 4], 2, 4, 3, [], 0
        ])


if __name__ == "__main__":
    ut.main()
