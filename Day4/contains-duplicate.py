from typing import *


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pointer = 0
        cursor = 0
        end = len(nums)
        while pointer != end - 1:
            cursor += 1
            if cursor == end:
                pointer += 1
                cursor = pointer + 1
            if pointer == end - 1:
                return  False
            if nums[pointer] == nums[cursor]:
                return True
        return False


test_solution = Solution()
# test_solution.containsDuplicate([1,2,3])
print(test_solution.containsDuplicate([1,2,1]))