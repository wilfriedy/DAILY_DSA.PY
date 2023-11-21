from typing import *

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums :
            return 0
        pointer = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[pointer] = nums[i]
                pointer += 1

        return pointer


test_nums = [0,1,2,2,3,0,4,2]
test_val = 2

print(Solution().removeElement(test_nums, test_val))

