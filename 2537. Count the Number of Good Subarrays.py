from typing import List
from collections import defaultdict
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        n = len(nums)
        sliderLeft, sliderRight = 0, 0
        curPairs = 0
        ans = 0
        while sliderRight < n:
            saveLeft = sliderLeft
            while sliderRight < n:
                num = nums[sliderRight]
                count = counts[num]
                curPairs += count
                counts[num] = count + 1
                sliderRight += 1
                if curPairs >= k:
                    break
            if sliderRight > n:
                break
            if curPairs < k:
                break
            while curPairs >= k:
                num = nums[sliderLeft]
                count = counts[num]
                if curPairs - count + 1 < k:
                    break
                curPairs -= count - 1
                counts[num] = count - 1
                sliderLeft += 1
            ans += (sliderLeft - saveLeft + 1) * (n - sliderRight + 1)
            num = nums[sliderLeft]
            count = counts[num]
            counts[num] = count - 1
            curPairs -= count - 1
            sliderLeft += 1
        return ans
    
s = Solution()
#print(s.countGood(nums = [1,1,1,1,1], k = 10)) # 1
#print(s.countGood(nums = [3,1,4,3,2,2,4], k = 2)) # 4
#print(s.countGood([2,3,3,3,3,1,3,1,3,2], 19)) # 0
print(s.countGood([2,1,3,1,2,2,3,3,2,2,1,1,1,3,1], 11)) #21
        
