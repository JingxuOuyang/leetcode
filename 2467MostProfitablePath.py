from typing import List

class Node:
    val : int

    def __init__(self, val):
        self.val = val
        self.nexts = []
        

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        nodes = []
        for i in range(n):
            nodes.append(Node(amount[i]))
        for edge in edges:
            nodes[edge[1]].nexts.append(edge[0])
            nodes[edge[0]].nexts.append(edge[1])
        pathToBob = []
        def findInNode(nodeid:int, fromId:int)->bool:
            if nodeid == bob:
                pathToBob.append(nodeid)
                return True
            for next in nodes[nodeid].nexts:
                if next == fromId:
                    continue
                if findInNode(next, nodeid):
                    pathToBob.append(nodeid)
                    return True
            return False
        findInNode(0, -1)
        pathLen = len(pathToBob)
        for i in range(pathLen // 2):
            nodes[pathToBob[i]].val = 0
        if pathLen % 2 == 1:
            nodes[pathToBob[pathLen // 2]].val >>= 1
        def walk(nodeid:int, fromid:int)->int:
            node = nodes[nodeid]
            if len(node.nexts) == 1 and node.nexts[0] == fromid:
                return node.val
            return node.val + max(walk(next, nodeid) for next in node.nexts if next != fromid)
                
        return walk(0, -1)

s = Solution()
print(s.mostProfitablePath(edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]))
# print(s.mostProfitablePath(edges = [[0,1]], bob = 1, amount = [-7280,2350]))
# edges =
# [[0,2],[0,5],[1,3],[1,5],[2,4]]
# bob =
# 4
# amount =
# [5018,8388,6224,3466,3808,3456]
#print(s.mostProfitablePath([[0,2],[0,5],[1,3],[1,5],[2,4]], 4, [5018,8388,6224,3466,3808,3456]))