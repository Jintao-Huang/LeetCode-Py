from leetcode_alg import *


class Solution:
    """类背包"""
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for capa in range(c, amount+1):
                dp[capa] += dp[capa-c]
        return dp[amount]


if __name__ == "__main__":
    amount = 5
    coins = [1, 2, 5]
    assert Solution().change(5, coins) == 4
