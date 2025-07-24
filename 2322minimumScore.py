from typing import List
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        # build tree
        n = len(nums)
        #nodes = [[nums[i], -1, []] for i in range(n)]
        routes = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]
            routes[u].append(v)
            routes[v].append(u)
        # find a root, apply post order walk
        root = 0
        postorderList = []
        node_parents = [-1] * n
        def postorder(node: int, from_node: int):
            node_parents[node] = from_node
            t = 0
            for child in routes[node]:
                if child == from_node:
                    continue
                t ^= postorder(child, node)
            t ^= nums[node]
            postorderList.append([t, node])
            return t
        postorder(root, -1)
        total_val = postorderList[-1][0]
        ans = 10**9
        for i in range(n - 2):
            val, node = postorderList[i][0], postorderList[i][1]
            node_parent = node_parents[node]
            residual_val = total_val ^ val
            for j in range(i + 1, n - 1):
                val2, node2 = postorderList[j][0], postorderList[j][1]
                if node2 == node_parent:
                    node_parent = node_parents[node_parent]
                    val2 ^= val                
                val3 = residual_val ^ val2
                score = max(val, val2, val3) - min(val, val2, val3)
                #print(f"node: {node}, node2: {node2}, val: {val}, val2: {val2}, val3: {val3}, score={score}")
                if score < ans:
                    ans = score
        return ans

s = Solution()
print(s.minimumScore(nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]])) #9
print(s.minimumScore(nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]])) #0
print(s.minimumScore([9,14,2,1], [[2,3],[3,0],[3,1]])) # 11