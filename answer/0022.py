
from leetcode_alg import *


def dfs(left: int, right: int, path: bytearray, res: List[str]) -> None:
    # right >= left >= 0
    if left+right == 0:
        res.append(path.decode())
        return
    #
    if left > 0:
        path.append(40)  # ord("(")
        dfs(left-1, right, path, res)
        path.pop()
    if right > left:  
        path.append(41)  # ord(")")
        dfs(left, right-1, path, res)
        path.pop()


class Solution:
    """回溯"""
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        dfs(n, n, bytearray(), res)
        return res


if __name__ == "__main__":
    assert Solution().generateParenthesis(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']
    print(ord("("))
    print(ord(")"))