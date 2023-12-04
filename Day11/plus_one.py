from typing import *

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitStr = ''
        finalDigits = []
        for i in range(len(digits)):
            digitStr += str(digits[i])

        newInt = int(digitStr) + 1

        for i in range(len(str(newInt))):
            finalDigits.append(int(str(newInt)[i]))

        return finalDigits

print(Solution().plusOne([9]))
