MOD = 10**9 + 7
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        dp = [1] * 26
        for i in range(t):
            idx = i % 26
            dp[idx] = (dp[idx] + dp[(idx + 1)% 26]) % MOD
        ans = 0
        for c in s:
            d = ord(c) - ord('a')
            ans = (ans + dp[(t + d) % 26]) % MOD
        return ans

s = Solution()
print(s.lengthAfterTransformations(s = "azbk", t = 1))
print(s.lengthAfterTransformations( s = "abcyy", t = 2))
print(s.lengthAfterTransformations())