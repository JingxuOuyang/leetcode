class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = 0
        val = 0
        mask = 1
        while mask <= k:
            mask <<= 1
        t = 0
        for c in s:
            t += 1
            val <<= 1
            if c == '1':
                val += 1
            if val > k:
                if val >= mask:
                    val -= mask
                else:
                    val -= (mask >> 1)
                t -= 1
                if t > ans:
                    ans = t
        if t > ans:
            return t
        return ans

s = Solution()
#print(s.longestSubsequence(s = "1001010", k = 5))
#print(s.longestSubsequence(s = "00101001", k = 1))
print(s.longestSubsequence(s='111000111', k=4)) #5