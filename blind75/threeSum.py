from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                         # sort to use two-pointers & skip dups
        n = len(nums)
        res = []

        for i in range(n):
            # If the current value > 0, remaining values are >= it, so sum can't be 0
            if nums[i] > 0:
                break

            # Skip duplicate 'i'
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # Move both pointers and skip duplicates
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return res


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
