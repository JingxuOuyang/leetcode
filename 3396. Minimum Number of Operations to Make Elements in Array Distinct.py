from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        visited = set()
        for i in range(n % 3):
            if nums[-i - 1] in visited:
                return (n + 2) // 3
            visited.add(nums[-i - 1])
        i = (n // 3) * 3
        while i > 0:
            for j in range(3):
                if nums[i - j - 1] in visited:
                    return i // 3
                visited.add(nums[i - j - 1])
            i -= 3
        return i // 3

s = Solution()
print(s.minimumOperations([1,2,3,4,2,3,3,5,7]))
