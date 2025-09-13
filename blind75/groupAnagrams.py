from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_group = {}

        for val in strs:

            sorted_val = "".join(sorted(val))

            if sorted_val in anagram_group:
                anagram_group[sorted_val].append(val)
            else:
                anagram_group[sorted_val] = [val]

        return list(anagram_group.values())


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
