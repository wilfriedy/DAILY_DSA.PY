from typing import  *

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums :
            return 0
        pointer = 0

