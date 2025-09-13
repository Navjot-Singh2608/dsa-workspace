from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for index, num in enumerate(nums):
            result = target - num
            if result in seen:
                return [seen[result], index]
            seen[num] = index

        return []


solution = Solution()
print(solution.twoSum([3, 4, 5, 6], 7))
