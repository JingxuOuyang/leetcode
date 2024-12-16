from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heapNums = list()
        for i, num in enumerate(nums):
            heapNums.append((num << 7) + i)
        heapq.heapify(heapNums)
        mask = (1 << 7) - 1
        for i in range(k):
            idx = (heapNums[0] & mask)
            nums[idx] *= multiplier
            heapq.heappushpop(heapNums, (nums[idx] << 7) + idx)
        return nums
    
if __name__ == '__main__':
    s = Solution()
    print(s.getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2))
    print(s.getFinalState(nums = [1,2], k = 3, multiplier = 4))