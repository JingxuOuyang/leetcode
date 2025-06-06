class Solution:
    def robotWithString(self, s: str) -> str:
        i = 0
        n = len(s)
        t = []
        ans = []
        while i < n:
            minIndex = i
            for j in range(i + 1, n):
                if ord(s[j]) <= ord(s[minIndex]):
                    minIndex = j
            while len(t) > 0 and ord(t[-1]) <= ord(s[minIndex]):
                ans.append(t.pop())
                
            for j in range(i, minIndex + 1):
                if ord(s[j]) == ord(s[minIndex]):
                    ans.append(s[j])
                else:
                    t.append(s[j])
            i = minIndex + 1
        for j in range(len(t) - 1, -1, -1):
            ans.append(t[j])

        return ''.join(ans)

s = Solution()
print(s.robotWithString("bccaddaffe")) # vxy
print(s.robotWithString('zza'))
print(s.robotWithString('bac'))
print(s.robotWithString('bdda'))