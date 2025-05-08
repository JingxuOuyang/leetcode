from typing import List
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        reached = list()
        reached.append((0, (0, 0), 2))
        visits = set()
        visits.add((0, 0))
        while len(reached) > 0:
            t, pos, lastuse = heappop(reached)
            if pos[0] < n - 1:
                next_pos = (pos[0] + 1, pos[1])
                if next_pos not in visits:
                    cost = 1 if lastuse == 2 else 2
                    reachTime = max(t, moveTime[next_pos[1]][next_pos[0]]) + cost
                    visits.add(next_pos)
                    if next_pos == (n - 1, m - 1):
                        return reachTime
                    else:
                        heappush(reached, (reachTime, next_pos, cost))
            if pos[0] > 0:
                next_pos = (pos[0] - 1, pos[1])
                if next_pos not in visits:
                    cost = 1 if lastuse == 2 else 2
                    reachTime = max(t, moveTime[next_pos[1]][next_pos[0]]) + cost
                    visits.add(next_pos)
                    if next_pos == (n - 1, m - 1):
                        return reachTime
                    else:
                        heappush(reached, (reachTime, next_pos, cost))
            if pos[1] < m - 1:
                next_pos = (pos[0], pos[1] + 1)
                if next_pos not in visits:
                    cost = 1 if lastuse == 2 else 2
                    reachTime = max(t, moveTime[next_pos[1]][next_pos[0]]) + cost
                    visits.add(next_pos)
                    if next_pos == (n - 1, m - 1):
                        return reachTime
                    else:
                        heappush(reached, (reachTime, next_pos, cost))
            if pos[1] > 0:
                next_pos = (pos[0], pos[1] - 1)
                if next_pos not in visits:
                    cost = 1 if lastuse == 2 else 2
                    reachTime = max(t, moveTime[next_pos[1]][next_pos[0]]) + cost
                    visits.add(next_pos)
                    if next_pos == (n - 1, m - 1):
                        return reachTime
                    else:
                        heappush(reached, (reachTime, next_pos, cost))
        return -1