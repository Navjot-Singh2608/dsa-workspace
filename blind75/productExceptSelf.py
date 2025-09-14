from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        for i in range(len(nums)):
            j = 0
            prod = 1
            while j < len(nums):

                if i != j:
                    prod *= nums[j]
                j += 1

            output.append(prod)

        return output


solution = Solution()
print(solution.productExceptSelf([-1, 0, 1, 2, 3]))
