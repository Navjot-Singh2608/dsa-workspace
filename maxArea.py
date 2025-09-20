from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:

        f = 0
        l = len(heights) - 1
        max_area = 0
        w = len(heights) - 1

        while f < l:

            min_h = min(heights[l], heights[f])

            max_area = max(max_area, min_h * w)

            if (heights[f] < heights[l]):
                f += 1
            else:
                l -= 1
            w -= 1

        return max_area


solution = Solution()
print(solution.maxArea([1, 7, 2, 5, 4, 7, 3, 6]))
