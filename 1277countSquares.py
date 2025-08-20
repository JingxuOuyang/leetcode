from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ranks = [[0 for i in range(n)] for j in range(m)]
        ans = 0
        for y in range(m):
            for x in range(n):
                if matrix[y][x] == 0:
                    continue
                possible_concat_rank = ranks[y-1][x-1] if x > 0 and y > 0 else 0
                y_rank = 0
                while y_rank < possible_concat_rank:
                    if matrix[y - y_rank - 1][x] == 0:
                        break
                    y_rank += 1
                x_rank = 0
                while x_rank < possible_concat_rank:
                    if matrix[y][x - x_rank - 1] == 0:
                        break
                    x_rank += 1
                final_rank = 1 + min(x_rank, y_rank, possible_concat_rank)
                #print(f"pos=({x},{y}),rank={final_rank}")
                ranks[y][x] = final_rank
                ans += final_rank
        return ans
    

s = Solution()
# print(s.countSquares([
#   [0,1,1,1,0],
#   [1,1,1,1,0],
#   [0,1,1,1,0]
# ]))
print(s.countSquares(matrix = [
    [1,0,1,0,1],
    [1,0,0,1,1],
    [0,1,0,1,1],
    [1,0,0,1,1]
])) # 14