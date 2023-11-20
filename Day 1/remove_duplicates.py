from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pointer = 0

        for i in range(1, len(nums)):
            if nums[pointer] != nums[i]:
                pointer += 1
                nums[pointer] = nums[i]
        return pointer + 1

testCase = Solution()
print(testCase.removeDuplicates([1,1,1,2,2,3,3,4,5,5,5]))