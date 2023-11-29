class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            "I": 1,
            'V': 5,
            'X': 10,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        size = len(s)
        result = 0
        if size == 1:
            return romanDict[s]
        pointer = 0

        while pointer < size:
            print(result, pointer)
            i = pointer + 1
            if i < size and str(s[pointer] + s[i]) in romanDict:
                result += romanDict[str(s[pointer] + s[i])]
                pointer = i + 1
            else:
                result += romanDict[s[pointer]]
                pointer += 1

        # **** first attempt *******
        # for i, int_p in enumerate(s):
        #     print(result)
        #     if i == size - 1 and romanDict[int_p]:
        #         result += romanDict[int_p]
        #         break
        #     if i + 1 < size and romanDict[str(int_p + s[i + 1])]:
        #         result += romanDict[str(int_p + s[i + 1])]
        #     else:
        #         result += romanDict[int_p]
        return result


print(Solution().romanToInt("MCMXCIV"))