class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashSet = {"}":"{", "]":"[", ")":"("}

        for i in s:
            if i in hashSet:
                if stack and stack[-1] == hashSet[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False

# ex = []
# if ex:
#     print('yes')
# else:
#     print('not')