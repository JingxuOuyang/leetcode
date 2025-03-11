class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i, j, n = 0, 0, len(s)
        na, nb, nc = 0, 0, 0
        ans = 0
        while i < n:
            while i < n:
                if s[i] == 'a':
                    na += 1
                elif s[i] == 'b':
                    nb += 1
                else:
                    nc += 1
                if na > 0 and nb > 0 and nc > 0:
                    break
                i += 1
            if na <= 0 or nb <= 0 or nc <= 0:
                break
            while True:
                if (s[j] == 'a' and na == 1) or (s[j] == 'b' and nb == 1) or (s[j] == 'c' and nc == 1):
                    break
                if s[j] == 'a':
                    na -= 1
                elif s[j] == 'b':
                    nb -= 1
                else:
                    nc -= 1
                j += 1
            ans += j + 1
            i += 1
        return ans

s = Solution()
print(s.numberOfSubstrings(s = "abcabc"))
print(s.numberOfSubstrings("abccc"))
print(s.numberOfSubstrings('aaacb'))