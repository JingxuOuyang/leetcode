import collections
class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter = collections.Counter()
        for i in range(1, n + 1):
            counter[sum([int(x) for x in str(i)])] += 1
        maxSize = max(counter.values())
        return sum(1 for v in counter.values() if v == maxSize)