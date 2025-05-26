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
        found = 0
        while q:
            u = q.popleft()
            dp[u][ord(colors[u]) - ord('a')] += 1
            found += 1
            for v in routes[u]:
                indegrees[v] -= 1
                for i in range(26):
                    dp[v][i] = max(dp[v][i], dp[u][i])
                if indegrees[v] == 0:
                    q.append(v)
        if found != n:
            return -1
        ans = 0
        for i in range(n):
            ans = max(ans, max(dp[i]))
        return ans