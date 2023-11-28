class Solution:
    def isPalindrome(self, x: int) -> bool:
        int_to_str = str(x)
        size = len(int_to_str)
        if size == 1:
            return True
        reverse_str = "",
        for i in int_to_str:
            reverse_str = i + reverse_str
        return reverse_str == int_to_str


print(Solution().isPalindrome(121))
