from typing import List
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        count = 1
        n = len(nums)
        for i in range(1, k - 1):
            if nums[i] == nums[i - 1] + 1:
                count += 1
            else:
                count = 1
        for i in range(n - k + 1):
            if nums[i + k - 1] == nums[i + k - 2] + 1:
                count += 1
            else:
                count = 1
            if count >= k:
                nums[i] = nums[i + k - 1]
            else:
                nums[i] = -1
        # for i in range(n - k + 1, n):
        #     nums[i] = -1
        return nums[:n-k+1]

# Input: nums = [1,2,3,4,3,2,5], k = 3

# Output: [3,4,-1,-1,-1]


# Input: nums = [2,2,2,2,2], k = 4

# Output: [-1,-1]

# Input: nums = [3,2,3,2,3,2], k = 2

# Output: [-1,3,-1,3,-1]
if __name__ == "__main__":
    s = Solution()
    print(s.resultsArray(nums = [1,2,3,4,3,2,5], k = 3))
    print(s.resultsArray(nums = [2,2,2,2,2], k = 4))
    print(s.resultsArray(nums = [3,2,3,2,3,2], k = 2))