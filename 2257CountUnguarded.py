from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        map = [0] * (m * n)
        for wall in walls:
            map[wall[0] * n + wall[1]] = 1
        for guard in guards:
            map[guard[0] * n + guard[1]] = 2
        for guard in guards:
            # left
            map[guard[0] * n + guard[1]] = 2
            for i in range(guard[1] - 1, -1, -1):
                if map[guard[0] * n + i] > 0:
                    break
                map[guard[0] * n + i] = -1
            for i in range(guard[1] + 1, n):
                if map[guard[0] * n + i] > 0:
                    break
                map[guard[0] * n + i] = -1
            for i in range(guard[0] - 1, -1, -1):
                if map[i * n + guard[1]] > 0:
                    break
                map[i * n + guard[1]] = -1
            for i in range(guard[0] + 1, m):
                if map[i * n + guard[1]] > 0:
                    break
                map[i * n + guard[1]] = -1
        return map.count(0)

if __name__ == '__main__':
    s = Solution()
    print(s.countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]))
    print(s.countUnguarded(m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]))