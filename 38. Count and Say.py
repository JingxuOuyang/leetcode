class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for i in range(n - 1):
            s2 = []
            j, n = 0, len(s)
            while j < n:
                start = j
                j += 1
                while j < n and s[j] == s[j - 1]:
                    j += 1
                s2.append(str(j - start))
                s2.append(s[j - 1])
            s3 = ''.join(s2)
            s = s3   
        return s

s = Solution()
print(s.countAndSay())