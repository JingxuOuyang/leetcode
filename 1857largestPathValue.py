from typing import List
from collections import deque
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        routes = [[] for _ in range(n)]
        indegrees = [0] * n
        for u, v in edges:
            indegrees[v] += 1
            routes[u].append(v)
        q = deque()
        dp = [[0] * 26 for _ in range(n)]
        for i in range(n):
            if indegrees[i] == 0:
                q.append(i)
        