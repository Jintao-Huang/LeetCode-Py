from leetcode_alg import *
import unittest as ut


class TestLL(ut.TestCase):
    def test_ll(self):
        res = []
        l = LinkedList([1, 2, 3])
        head, tail = l.head, l.tail
        l.insert_between(tail.prev, LinkedListNode(4), tail)
        l.remove(head.next)
        res.append(l.tolist())
        res.append(head.next.val)
        res.append(tail.prev.val)
        self.assertTrue(res == [
            [2, 3, 4], 2, 4
        ])


if __name__ == "__main__":
    ut.main()
