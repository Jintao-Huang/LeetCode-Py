from leetcode_alg import *
import unittest as ut
import json


class TestToLL(ut.TestCase):
    def test_to_ll(self):
        l = [1, 2, 3, 4, 5]
        ll = to_linkedlist(l)
        self.assertTrue(from_linkedlist(ll) == l)


class TestToTree(ut.TestCase):
    def test_to_tree(self):
        root = "[5,1,2,3,null,6,4]"
        tree = to_tree(root)
        self.assertTrue(from_tree(tree) == json.loads(root))


if __name__ == "__main__":
    ut.main()
