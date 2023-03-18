from leetcode_alg import *


class Solution:
    """贪心, 双指针. recommended"""

    def trap(self, height: List[int]) -> int:
        lo, hi = 0, len(height)-1
        max_left, max_right = 0, 0
        res = 0
        while lo <= hi:
            loH, hiH = height[lo], height[hi]
            if loH <= hiH:
                if max_left < loH:
                    max_left = loH
                else:
                    res += max_left - loH
                lo += 1
            else:
                if max_right < hiH:
                    max_right = hiH
                else:
                    res += max_right - hiH
                hi -= 1
        return res


class Solution2:
    """动态规划"""

    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        #
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])
        #
        max_right = 0
        res = 0
        for i in reversed(range(n)):
            if height[i] > max_right:
                max_right = height[i]
            res += min(max_left[i], max_right) - height[i]
        return res


class Solution3:
    """单调栈"""

    def trap(self, height: List[int]) -> int:
        next_ge, prev_gt = monotone_stack3(height, "ge")
        n = len(height)
        res = 0
        for i in range(1, n-1):
            j, k = prev_gt[i], next_ge[i]
            if j != -1 and k != -1:
                w = k - j - 1
                h = min(height[j], height[k]) - height[i]
                res += h * w
        return res


class Solution4:
    """单调栈优化. 两次遍历变一次遍历"""

    def trap(self, height: List[int]) -> int:
        # 不需要边界处理.
        res = 0
        stack = []
        for i, x in enumerate(height):
            # lo..idx..i
            while stack and ge(x, height[stack[-1]]):
                idx = stack.pop()
                if len(stack) == 0:
                    break
                lo = stack[-1]
                w = i - lo - 1
                h = min(x, height[lo]) - height[idx]
                res += h * w
            stack.append(i)
        return res


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert Solution().trap(height) == 6
    assert Solution2().trap(height) == 6
    assert Solution3().trap(height) == 6
    assert Solution4().trap(height) == 6
