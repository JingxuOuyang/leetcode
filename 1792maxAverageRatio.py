from typing import List
import heapq

class Entry:
    def __init__(self, p:int, t:int):
        self.p = p
        self.t = t
    
    def __lt__(self, other:'Entry'):
        return (other.t + 1) * other.t * (self.t - self.p) > (self.t + 1) * self.t * (other.t - other.p)

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = [Entry(cls[0], cls[1]) for cls in classes]
        heapq.heapify(pq)
        for _ in range(extraStudents):
            heapq.heapreplace(pq, Entry(pq[0].p + 1, pq[0].t + 1))
        return sum(e.p / e.t for e in pq) / len(pq)

s = Solution()
print(s.maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2))
print(s.maxAverageRatio(classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4))