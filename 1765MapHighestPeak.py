from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        cur = []
        ans = []
        for y in range(m):
            ans.append([])
            for x in range(n):
                if isWater[y][x] == 1:
                    cur.append((x, y))
                    ans[-1].append(0)
                else:
                    ans[-1].append(-1)
        while len(cur) > 0:
            next = []
            for x, y in cur:
                if x > 0:
                    if ans[y][x - 1] == -1:
                        next.append((x - 1, y))
                        ans[y][x - 1] = ans[y][x] + 1
                if x < n - 1:
                    if ans[y][x + 1] == -1:
                        next.append((x + 1, y))
                        ans[y][x + 1] = ans[y][x] + 1
                if y > 0:
                    if ans[y - 1][x] == -1:
                        next.append((x, y - 1))
                        ans[y - 1][x] = ans[y][x] + 1
                if y < m - 1:
                    if ans[y + 1][x] == -1:
                        next.append((x, y + 1))
                        ans[y + 1][x] = ans[y][x] + 1
            cur = next
        return ans

if __name__ == '__main__':
    s = Solution()
    #print(s.highestPeak(isWater = [[0,1],[0,0]]))
    print(s.highestPeak(isWater = [[0,0,1],[1,0,0],[0,0,0]]))
