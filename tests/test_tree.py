from leetcode_alg import *
import unittest as ut

class TestTree(ut.TestCase):
    def test_traversal(self):
        root: TreeNode = to_tree("[1, 2, 3, 4, null, null, 5]")
        res = []
        preorder_traversal(root, res)
        res2 = preorder_traversal2(root)
        self.assertTrue(res == res2)
        #
        res = []
        inorder_traversal(root, res)
        res2 = inorder_traversal2(root)
        self.assertTrue(res == res2)
        #
        res = []
        postorder_traversal(root, res)
        res2 = postorder_traversal2(root)
        self.assertTrue(res == res2)


if __name__ == "__main__":
    ut.main()
