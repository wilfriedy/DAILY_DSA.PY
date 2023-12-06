from typing import *


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        hashSet = {'+', "D", 'C'}
        rec = []

        for i, el in enumerate(operations):
            print(rec)
            if el in hashSet:
                if rec and rec[-1] not in hashSet:
                    if el == 'C':
                        rec.pop()
                    if el == 'D':
                        rec.append(int(rec[-1] * 2))
                    if el == '+':
                        if len(rec) > 1:
                            rec.append(int(rec[-1]) + int(rec[-2]))
                        else:
                            rec.append(rec[-1] + rec[-1])

                        # rec[-1] += rec[-1] + rec[-2] if len(rec) > 1 else rec[1]
            else:
                rec.append(int(el))

        # print(rec)
        record_size = len(rec)
        if not rec:
            return 0
        if record_size < 2:
            return rec[0]
        total = 0
        for _, el in enumerate(rec):
            total += el

        return total


print(Solution().calPoints(["5", "2", "C", "D", "+"]))
