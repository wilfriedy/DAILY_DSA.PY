from typing import *

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_len = len(s)
        if str_len != len(t):
            return False
        if str_len == 1:
            return s[0] == t[0]
        for i in range(len(t)):
            if t[i] not in s:
                return False
        return True


test_solution = Solution()
print(test_solution.isAnagram("anagram","nagaram"))
# print(test_solution.isAnagram("a","d"))