from typing import List
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        maxSolved = 0
        ans = 0
        for i, question in enumerate(questions):
            points = maxSolved + question[0]
            if points > ans:
                ans = points
            if i + question[1] < n and dp[i + question[1]] < points:
                dp[i + question[1]] = points
            if dp[i] > 0 and dp[i] > maxSolved:
                maxSolved = dp[i]
        return ans

s = Solution()
print(s.mostPoints(questions = [[3,2],[4,3],[4,4],[2,5]]))
print(s.mostPoints(questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]))