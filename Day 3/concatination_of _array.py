from typing import *

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0
        ans = []
        counter = 0
        num_len = len(nums)
        print(num_len)
        for  i in range(num_len * 2):
            print(counter, i)
            if i >= (num_len):
                ans.append(nums[counter])
                print(counter, 'shdjsdu++++++++++++')
                counter += 1
                print(counter, 'shdjsdu++++++++++++')
            if i < num_len:
                print(i, 'rrr')
                ans.append(nums[i])
                print(ans, 'dhdsjdskjkj')

        return  ans


test_solution = Solution()
# test_solution.getConcatenation([1,2,3])
print(test_solution.getConcatenation([1,2,1]))

