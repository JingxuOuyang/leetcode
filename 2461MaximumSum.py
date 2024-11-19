from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counts = dict()
        repeatSet = set()
        sum = 0
        for i in range(k - 1):
            sum += nums[i]
            if nums[i] in counts:
                counts[nums[i]] += 1
                repeatSet.add(nums[i])
            else:
                counts[nums[i]] = 1
        n = len(nums)
        ans = 0
        for i in range(n - k + 1):
            lastNum = nums[i + k - 1]
            if lastNum in counts:
                counts[lastNum] += 1
                repeatSet.add(lastNum)
            else:
                counts[lastNum] = 1
            sum += lastNum
            if len(repeatSet) == 0:
                if sum > ans:
                    ans = sum
            numi = nums[i]
            counts[numi] -= 1
            iCount = counts[numi]
            if iCount == 0:
                del counts[numi]
            elif counts[numi] == 1:
                repeatSet.remove(numi)
            sum -= numi
        return ans

if __name__ == "__main__":
    s = Solution()
  #  print(s.maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3))
  #  print(s.maximumSubarraySum([4,4,4], 3))
    print(s.maximumSubarraySum([5,3,3,1,1], 3))