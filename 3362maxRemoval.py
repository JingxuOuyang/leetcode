from typing import List
from heapq import heappush, heappop
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        queries.sort(key=lambda x:x[0])
        deltaArray = [0] * n
        used = 0
        j = 0
        hp = []
        for i, num in enumerate(nums):
            while j < len(queries) and queries[j][0] == i:
                heappush(hp, -queries[j][1])
                j += 1
            for k in range(num - used):
                if len(hp) == 0 or -hp[0] < i:
                    return -1
                deltaArray[-heappop(hp)] += 1
                used += 1
            used -= deltaArray[i]
        return len(hp)

if __name__ == '__main__':
    s = Solution()
    print(s.maxRemoval(nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]))
    #print(s.maxRemoval(nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]))
    #print(s.maxRemoval([1,0], [[1,1],[1,1],[1,1],[0,1],[0,1]]))
    #print(s.maxRemoval([1,2], [[1,1],[0,0],[1,1],[1,1],[0,1],[0,0]]))
