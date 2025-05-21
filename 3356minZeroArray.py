from typing import List
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        ans = 0
        n, m = len(nums), len(queries)
        stk = [0] * (n + 1)
        val = 0
        for i, num in enumerate(nums):
            val += stk[i]
            while ans < m and val < num:
                query = queries[ans]
                if query[1] < i:
                    ans += 1
                    continue
                stk[query[0]] += query[2]
                stk[query[1] + 1] -= query[2]
                if query[0] <= i:
                    val += query[2]
                ans += 1
            if ans == m and val < num:
                return -1
        return ans   
                
if __name__ == "__main__":
    s = Solution()
    print(s.minZeroArray(nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]))
    print(s.minZeroArray(nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]))
    print(s.minZeroArray([5], [[0,0,5],[0,0,1],[0,0,3],[0,0,2]]))