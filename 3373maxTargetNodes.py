from typing import List
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def dfs(routes: List[List[int]], node: int, from_node: int, color: bool, color_map: List[False]):
            color_map[node] = color
            for route in routes[node]:
                if route == from_node:
                    continue
                dfs(routes, route, node, not color, color_map)

        def build(edges: List[List[int]])-> List[int]:
            n = len(edges) + 1
            colors = [False] * n
            routes = [[] for _ in range(n)]
            for edge in edges:
                routes[edge[0]].append(edge[1])
                routes[edge[1]].append(edge[0])
            dfs(routes, 0, -1, True, colors)
            return colors
        
        colors1 = build(edges1)
        colors2 = build(edges2)
        n, m = len(edges1) + 1, len(edges2) + 1
        redNodes1, redNodes2 = colors1.count(True), colors2.count(True)
        blueNodes1, blueNodes2 = n - redNodes1, m - redNodes2
        appendNodes = max(redNodes2, blueNodes2)
        ans = [0] * n
        for i in range(n):
            if colors1[i]:
                ans[i] = appendNodes + redNodes1
            else:
                ans[i] = appendNodes + blueNodes1
        return ans