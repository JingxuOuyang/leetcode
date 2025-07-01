class Solution:
    def possibleStringCount(self, word: str) -> int:
        i, n = 0, len(word)
        ans = 1
        while i < n:
            j = i + 1
            while j < n and word[j] == word[j - 1]:
                j += 1
            t = j - i
            i = j
            if t == 1:
                continue
            ans += t - 1
        return ans

s = Solution()
print(s.possibleStringCount("abbcccc"))