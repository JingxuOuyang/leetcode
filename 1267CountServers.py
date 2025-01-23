from typing import List
class RowNetwork:
    link:int

class ColumnNetwork:
    payload:int
    links:List[int]

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        isolated_servers = []
        col_counts = [0] * n
        ans = 0
        for y in range(m):
            server_in_row = 0
            last_server_col = -1
            for x in range(n):
                if grid[y][x] == 1:
                    server_in_row += 1
                    col_counts[x] += 1
                    last_server_col = x
            if server_in_row == 1:
                isolated_servers.append(last_server_col)
            elif server_in_row > 1:
                ans += server_in_row
        for isolated_server in isolated_servers:
            if col_counts[isolated_server] > 1:
                ans += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.countServers(grid = [[1,0],[0,1]]))
    print(s.countServers(grid = [[1,0],[1,1]]))