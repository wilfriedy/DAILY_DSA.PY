from typing import *

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return  False
        for i in range(len(t) - 1):
            if t[i] not in s:
                return False
        return True
