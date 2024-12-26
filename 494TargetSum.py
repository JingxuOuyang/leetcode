from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        numSum = sum(nums)
        delta = numSum - target
        if delta % 2 != 0:
            return 0
        delta //= 2
        nums.sort()
        
        def findDelta(leftNum:int, startIdx:int):
            count = 0
            for i in range(startIdx, len(nums)):
                if nums[i] > leftNum:
                    break
                if nums[i] == leftNum:
                    count += 1
                count += findDelta(leftNum - nums[i], i + 1)
            return count
        ans = findDelta(delta, 0)
        if numSum == target:
            ans += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    #print(s.findTargetSumWays(nums = [1,1,1,1,1], target = 3))
    print(s.findTargetSumWays([1,0,0], 1))