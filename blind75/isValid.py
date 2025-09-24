class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapping = {"(": ")", "{": "}", "[": "]"}

        for ch in s:
            if ch in mapping:
                stack.append(ch)
            else:
                if not stack or mapping[stack.pop()] != ch:
                    return False

        if len(stack) > 0:
            return False
        return True


solution = Solution()
print(solution.isValid("({[]})"))
