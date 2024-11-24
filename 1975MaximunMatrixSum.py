from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minAbsNum = 100001
        maxNegtiveNumber = -100001
        m, n = len(matrix), len(matrix[0])
        sum = 0
        nagtiveCount = 0
        for y in range(m):
            for x in range(n):
                num = matrix[y][x]
                if num > 0:
                    sum += num
                    continue
                sum -= num
                if num > maxNegtiveNumber:
                    maxNegtiveNumber = num
                nagtiveCount += 1
        if nagtiveCount % 2 == 0:
            return sum
        return sum + maxNegtiveNumber

if __name__ == "__main__":
    s = Solution()
    print(s.maxMatrixSum([[1,-1],[-1,1]]))