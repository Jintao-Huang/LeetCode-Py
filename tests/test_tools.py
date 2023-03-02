from leetcode_alg import *
import unittest as ut


class TestToLL(ut.TestCase):
    def test_to_ll(self):
        l = [1, 2, 3, 4, 5]
        ll = to_linkedlist(l)
        self.assertTrue(from_linkedlist(ll) == l)


if __name__ == "__main__":
    ut.main()
