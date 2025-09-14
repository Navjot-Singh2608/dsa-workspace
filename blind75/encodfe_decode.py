from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:

        decoded, i = [], 0

        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1  # move past '#'
            decoded.append(s[i:i+length])
            i += length  # move to the next length
        return decoded
