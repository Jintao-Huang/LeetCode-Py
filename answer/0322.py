
from leetcode_alg import *


class Solution:
    """recommended. 背包"""

    def coinChange(self, coins: List[int], amount: int) -> int:
        init_value = INF
        res = knapsack(coins, amount, False, "min", True, init_value)
        return res if res != init_value else -1


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        init_value = INF
        res = knapsack_C(coins, amount, "min", True, init_value)
        return res if res != init_value else -1


class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        init_value = INF
        n = len(coins)
        res = knapsackV(coins, amount, [1] * n, False, "min", True, init_value)
        return res if res != init_value else -1


class Solution4:
    def coinChange(self, coins: List[int], amount: int) -> int:
        init_value = INF
        n = len(coins)
        res = knapsackV_C(coins, amount, [1] * n, "min", True, init_value)
        return res if res != init_value else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    assert Solution().coinChange(coins, amount) == 3
    assert Solution2().coinChange(coins, amount) == 3
    assert Solution3().coinChange(coins, amount) == 3
    assert Solution4().coinChange(coins, amount) == 3

