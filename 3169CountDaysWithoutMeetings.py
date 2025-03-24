from typing import List
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x : x[0])
        lastday, ans = 0, 0
        for start, end in meetings:
            if start > lastday:
                ans += start - lastday - 1
            if end > lastday:
                lastday = end
        return ans + days - lastday

s = Solution()
print(s.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]]))
print(s.countDays(days = 5, meetings = [[2,4],[1,3]]))
print(s.countDays(days = 6, meetings = [[1,6]]))
print(s.countDays(days=10, meetings=[[1,8], [2,3], [3,6]]))