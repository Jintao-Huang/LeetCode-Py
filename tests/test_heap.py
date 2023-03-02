from leetcode_alg import *

if __name__ == "__main__":
    mpq = Heap2([])
    mpq.push((1, 5))
    mpq.push((2, 4))
    mpq.push((3, 4))
    mpq.push((4, 6))
    mpq.push((5, 1))
    print(mpq._id2pos)
    print(mpq.heap)
    print(mpq.pop())
    print(mpq._id2pos)
    print(mpq.heap)
    mpq.push((1, 0))
    print(mpq._id2pos)
    print(mpq.heap)
    mpq.push((1, 5))
    print(mpq._id2pos)
    print(mpq.heap)
"""
{1: 4, 2: 1, 3: 2, 4: 3, 5: 0}
[(5, 1), (2, 4), (3, 4), (4, 6), (1, 5)]
(5, 1)
{1: 1, 2: 0, 3: 2, 4: 3}
[(2, 4), (1, 5), (3, 4), (4, 6)]
{1: 0, 2: 1, 3: 2, 4: 3}
[(1, 0), (2, 4), (3, 4), (4, 6)]
{1: 1, 2: 0, 3: 2, 4: 3}
[(2, 4), (1, 5), (3, 4), (4, 6)]
"""