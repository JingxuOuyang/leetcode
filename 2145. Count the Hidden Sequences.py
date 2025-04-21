from typing import List
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        minval, maxval, val = 0, 0, 0
        for difference in differences:
            val += difference
            if val < minval:
                minval = val
            if val > maxval:
                maxval = val
        if upper - lower < maxval - minval:
            return 0
        return upper - lower - (maxval - minval) + 1