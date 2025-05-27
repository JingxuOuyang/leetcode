
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        t = n // m
        sum1, sum2 = (1 + t) * t *m, (1 + n) * n // 2
        return sum2 - sum1           