class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        last = {}
        left = 0
        best_len = 0

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right
            best_len = max(best_len, right - left + 1)

        return best_len


solution = Solution()
print(solution.lengthOfLongestSubstring("dvdf"))
