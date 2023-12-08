class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newStr = s.strip().split(" ")
        return len(newStr[-1])
