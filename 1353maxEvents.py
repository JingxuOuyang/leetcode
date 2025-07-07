from typing import List
from collections import Counter
from heapq import heappush, heappop

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        max_day = max(event[1] for event in events)
        events.sort()
        pq = []
        ans, j = 0, 0
        for i in range(1, max_day + 1):
            while j < n and events[j][0] <= i:
                heappush(pq, events[j][1])
                j += 1
            while pq and pq[0] < i:
                heappop(pq)
            if pq:
                heappop(pq)
                ans += 1
                
        return ans

s = Solution()
print(s.maxEvents(events = [[1,2],[2,3],[3,4]]))#3
print(s.maxEvents(events= [[1,2],[2,3],[3,4],[1,2]])) #4
print(s.maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]])) #4
print(s.maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]])) #5