from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        nums = sorted(set(nums))
        best = cur = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                cur += 1
            else:
                best = max(best, cur)
                cur = 1
        return max(best, cur)


solution = Solution()
print(solution.longestConsecutive([2, 20, 4, 10, 3, 4, 5]))
