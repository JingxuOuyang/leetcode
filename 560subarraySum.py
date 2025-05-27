from typing import List
from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = Counter()
        counter[0] += 1
        ans, cur_sum = 0, 0
        for num in nums:
            ans += counter[cur_sum + num - k]
            cur_sum += num
            counter[cur_sum] += 1
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1,1,1], 2)) # 2
    print(s.subarraySum([1], 0))
#    print(s.subarraySum([1,2,1,2,1], 3)) # 4
