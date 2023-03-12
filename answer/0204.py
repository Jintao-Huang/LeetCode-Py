from leetcode_alg import *


class Solution:
    def countPrimes(self, n: int) -> int:
        n -= 1
        if n < 2:
            return 0
        return sum(find_primes(n))


class Solution2:
    def countPrimes(self, n: int) -> int:
        res = 0
        for x in range(n):
            res += is_prime(x)
        return res


if __name__ == "__main__":
    n = 10
    assert Solution().countPrimes(n) == 4
    assert Solution2().countPrimes(n) == 4
