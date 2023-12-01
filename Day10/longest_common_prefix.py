from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ''
        size = len(strs)
        ping = 0
        for i, el in enumerate(strs[0]):
            for j in range(1, size):
                print(strs[j][i])
                if el == strs[j][i] and j < size - 1:
                    ping = 1
                if el != strs[j][i]:
                    ping = 0
                    break
                if el == strs[j][i] and j == size - 1:
                    # print(el)
                    common_prefix += el

            if ping == 0:
                break

        return common_prefix

print(Solution().longestCommonPrefix(["aa","aa"]))
