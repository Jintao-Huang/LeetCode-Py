from leetcode_alg import *


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def cond(mid: int) -> bool:
            time = 0  # 需要花费的时间
            for x in piles:
                time += ceil(x/mid)  # (x-1)//mid+1
                # if time > h:
                #     return False
            return time <= h
        return lower_bound(1, max(piles), cond)


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    assert Solution().minEatingSpeed(piles, h) == 4
