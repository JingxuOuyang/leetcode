from typing import List
from collections import Counter
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counts = [0] * 10
        for digit in digits:
            counts[digit] += 1
        digitSet = []
        for i, count in enumerate(counts):
            if count == 0:
                continue
            digitSet.append(i)
        ans = []
        for digit in digitSet:
            if digit == 0:
                continue
            for digit1 in digitSet:
                if digit1 == digit and counts[digit] == 1:
                    continue
                for digit2 in digitSet:
                    if digit2 % 2 != 0:
                        continue
                    if (counts[digit2] == 1 and (digit2 == digit or digit2 == digit1)) or (counts[digit2] == 2 and digit1 == digit2 and digit2 == digit):
                        continue
                    ans.append(digit * 100 + digit1 * 10 + digit2)
        return ans

s = Solution()
print(s.findEvenNumbers(digits = [2,1,3,0]))