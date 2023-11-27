from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # pointer = 0
        # i = 1
        # if len(nums) == 2 :
        #     return [nums[0], nums[1]]
        # while pointer != len(nums) - 1 :
        #     print(i)
        #     if i == len(nums) - 1:
        #         pointer += 1
        #         i = pointer + 1
        #     if nums[pointer] + nums[i] == target:
        #         break
        #     i += 1
        # return [pointer ,i]
        #************** second **************
        # pointer = 0
        # i = 1
        # if len(nums) == 2 :
        #     return [0, 1]
        # while pointer != len(nums) - 1 :
        #     print(i)
        #     if i == len(nums) - 1 & pointer < len(nums) - 1:
        #         pointer += 1
        #         i = pointer + 1
        #     if nums[pointer] + nums[i] == target:
        #         return [i, pointer]
        #     i += 1
        # return []
        for i in range(len(nums)):
            for j in range(i+ 1, len(nums)):
                if nums[i] == nums[j]:
                    return [i, j]
        return []


testing = Solution().twoSum([3,2,3], 6)
# testing = Solution().twoSum([1,3,4,2], 5)
print(testing)
