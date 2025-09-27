from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        counter = 0

        for num in sorted(nums):

            if counter != num:
                return counter

            counter += 1
