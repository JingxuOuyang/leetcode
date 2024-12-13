from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        indexArr = list(range(n))
        indexArr.sort(key=lambda i: nums[i])
        markedArr = [False] * n
        score = 0
        for i in indexArr:
            if markedArr[i]:
                continue
            score += nums[i]
            markedArr[i] = True
            if i > 0:
                markedArr[i - 1] = True
            if i < n - 1:
                markedArr[i + 1] = True
        return score
    
if __name__ == '__main__':
    s = Solution()
    print(s.findScore(nums = [2,1,3,4,5,2]))
    print(s.findScore(nums = [2,3,5,1,3,2]))