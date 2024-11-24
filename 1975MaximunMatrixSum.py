from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negtiveSum, sum = 0, 0
        minNum, maxNegtiveNum = 100001, -100001
        m, n = len(matrix), len(matrix[0])
        nagtiveCount = 0
        for y in range(m):
            for x in range(n):
                num = matrix[y][x]
                if num > 0:
                    sum += num
                    if num < minNum:
                        minNum = num
                else:
                    negtiveSum += num
                    if num > maxNegtiveNum:
                        maxNegtiveNum = num
                    nagtiveCount += 1
        if nagtiveCount % 2 == 0:
            return sum - negtiveSum
        if minNum < -maxNegtiveNum:
            return sum - negtiveSum - 2*minNum
        else:
            return sum - negtiveSum + 2*maxNegtiveNum

if __name__ == "__main__":
    s = Solution()
    print(s.maxMatrixSum([[1,-1],[-1,1]]))