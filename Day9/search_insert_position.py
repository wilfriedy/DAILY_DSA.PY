from typing import *

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        actual_index = 0
        for ind,el in enumerate(nums):
            if el == target :
                return ind
            if el < target :
                actual_index = ind + 1
        return actual_index


print(Solution().searchInsert([1,3,5,6], 4))