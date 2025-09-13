from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for value in nums:
            if value in seen:
                return True
            seen.add(value)

        return False


# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         has_duplicate = {}

#         for value in nums:
#             is_exist = has_duplicate.get(value)
#             if is_exist is None:
#                 has_duplicate[value] = 1
#             else:
#                 return True

#         return False


solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 3]))
