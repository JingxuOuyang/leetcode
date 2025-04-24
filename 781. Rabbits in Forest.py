from typing import List
from collections import Counter
import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        counter = Counter()
        for answer in answers:
            counter[answer] += 1
        for answer, count in counter.items():
            ans += math.ceil(count / (answer + 1)) * (answer + 1)
        return ans

s = Solution()
print(s.numRabbits(answers =[1,1,2]))