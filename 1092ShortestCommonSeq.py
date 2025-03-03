
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        dp = []
        for i in range(n1):
            dp.append([0] * (n2 + 1))
        dp.append([])
        for i in range(n2, -1, -1):
            dp[-1].append(i)
        for i in range(n1):
            dp[i][-1] = n1 - i
        for j in range(n1 - 1, -1, -1):
            for i in range(n2 - 1, -1, -1):
                if str1[j] == str2[i]:
                    dp[j][i] = 1 + dp[j + 1][i + 1]
                else:
                    dp[j][i] = min(dp[j + 1][i], dp[j][i + 1]) + 1
        ans = []
        i, j = 0, 0
        while i < n1 and j < n2:
            if str1[i] == str2[j]:
                ans.append(str1[i])
                i += 1
                j += 1
            else:
                if dp[i][j + 1] < dp[i + 1][j]:
                    ans.append(str2[j])
                    j += 1
                else:
                    ans.append(str1[i])
                    i += 1
        if i == n1:
            if j == n2:
                return "".join(ans)
            return "".join(ans) + str2[j:]
        else:
            return "".join(ans) + str1[i:]

s = Solution()
# print(s.shortestCommonSupersequence(str1 = "abac", str2 = "cab"))
# print(s.shortestCommonSupersequence(str1 = "aaaaaaaa", str2 = "aaaaaaaa"))
# Input
# str1 =
# "aabbabaa"
# str2 =
# "aabbbbbbaa"

# Use Testcase
# Output
# "aabbababbbaa"
# Expected
# "aabbbbbabaa"
print(s.shortestCommonSupersequence("aabbabaa", "aabbbbbbaa"))