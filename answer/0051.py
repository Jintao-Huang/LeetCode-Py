
from leetcode_alg import *


def decode_n_queens(res_raw: List[List[int]]) -> List[List[str]]:
    if len(res_raw) == 0:
        return []
    n = len(res_raw[0])
    line = bytearray(b".")
    line *= n
    ord_Q, ord_dot = ord("Q"), ord(".")
    res = []
    #
    for rr in res_raw:
        r = []  # res
        for i in rr:
            line[i] = ord_Q
            r.append(line.decode())
            line[i] = ord_dot
        res.append(r)
    return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res_raw = n_queens(n)
        res = decode_n_queens(res_raw)
        return res


if __name__ == "__main__":
    n = 4
    print(Solution().solveNQueens(n))
