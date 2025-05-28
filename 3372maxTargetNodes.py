from typing import List
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def dfs(routes: List[List[int]], from_node: int, node:int, k: int) -> int:
            if k < 0:
                return 0
            nexts = routes[node]
            ret = 1
            for next_node in nexts:
                if next_node == from_node:
                    continue
                ret += dfs(routes, node, next_node, k-1)
            return ret
        def build(edges: List[List[int]], k: int) -> List[int]:
            n = len(edges) + 1
            routes = [[] for _ in range(n)]
            for u, v in edges:
               routes[u].append(v)
               routes[v].append(u)
            res = [0] * n
            for i in range(n):
                res[i] = dfs(routes, -1, i, k)
            return res
        
        counts1 = build(edges1, k)
        counts2 = build(edges2, k - 1)
        maxCount2 = max(counts2)
        n = len(edges1) + 1
        ans = [0] * n
        for i in range(n):
            ans[i] = counts1[i] + maxCount2
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2)) # [9,7,9,8,8]

