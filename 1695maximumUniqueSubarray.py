from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        visited = set()
        l_slider, r_slider = 0, 0
        n = len(nums)
        score = 0
        ans = 0
        while r_slider < n:
            num = nums[r_slider]
            if num not in visited:
                visited.add(num)
                r_slider += 1
                score += num
            else:
                if score > ans:
                    ans = score
                while l_slider < r_slider:
                    num2 = nums[l_slider]
                    if num2 == num:
                        break
                    visited.remove(num2)
                    score -= num2
                    l_slider += 1
                #score -= num
                l_slider += 1
                r_slider += 1
        if score > ans:
            ans = score
        return ans
    
s = Solution()
print(s.maximumUniqueSubarray([4,2,4,5,6]))