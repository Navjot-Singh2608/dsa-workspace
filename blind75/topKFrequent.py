from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequent_elements = {}
        output = []

        for num in nums:
            frequent_elements[num] = frequent_elements.get(num, 0) + 1

        sorted_frequent_ele = sorted(
            frequent_elements.items(), key=lambda x: x[1], reverse=True)

        print(sorted_frequent_ele)

        for i in range(len(sorted_frequent_ele)):

            if k == 0:
                break
            output.append(sorted_frequent_ele[i][0])
            k -= 1

        return output


solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
