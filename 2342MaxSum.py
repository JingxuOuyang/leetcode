from typing import List
from collections import defaultdict

def digitSum(num:int)->int:
    ret = 0
    while num > 0:
        ret += num % 10
        num //= 10
    return ret

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        buckets = defaultdict(lambda:[0,0])
        ans = -1
        for num in nums:
            t = digitSum(num)
            p = buckets[t]
            if num <= p[1]:
                continue
            if num <= p[0]:
                p[1] = num
            else:
                p[1] = p[0]
                p[0] = num
            if p[0] > 0 and p[1] > 0:
                s = p[0] + p[1]
                if s > ans:
                    ans = s
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maximumSum(nums = [18,43,36,13,7]))
    print(s.maximumSum(nums = [10,12,19,14]))