from typing import List
from collections import defaultdict

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2:
            return node1
        visited1, visited2 = dict(), dict()
        cur = node1
        step = 0
        while cur != -1 and cur not in visited1:
            visited1[cur] = step
            step += 1
            cur = edges[cur]
        cur = node2
        step = 0
        while cur != -1 and cur not in visited2:
            visited2[cur] = step
            step += 1
            cur = edges[cur]
        ans = 10**5 + 1
        node_ans = -1
        for node1, step1 in visited1.items():
            if node1 in visited2:
                val = max(step1, visited2[node1])
                if val < ans or (val == ans and node1 < node_ans):
                    ans = val
                    node_ans = node1
        # if ans == 10**5 + 1:
        #     return -1
        return node_ans

if __name__ == "__main__":
    s = Solution()
    #print(s.closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1))
    #print(s.closestMeetingNode([5,3,1,0,2,4,5],3,2)) #3
    print(s.closestMeetingNode([4,4,8,-1,9,8,4,4,1,1], 5,6)) #1
    print(s.closestMeetingNode([2,0,0],2,0))
