class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_char = {}
        t_char = {}

        for val in s:
            is_exist = s_char.get(val)

            if is_exist is None:
                s_char[val] = 1
            else:
                s_char[val] += 1

        for val in t:
            is_exist = t_char.get(val)

            if is_exist is None:
                t_char[val] = 1
            else:
                t_char[val] += 1

        for key, value in s_char.items():

            if s_char[key] != t_char[key]:
                return False

        return True


solution = Solution()
print(solution.isAnagram("racecar"))
