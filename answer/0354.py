
from leetcode_alg import *

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        return LIS([e[1] for e in envelopes])

if __name__ == "__main__":
    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    print(Solution().maxEnvelopes(envelopes))