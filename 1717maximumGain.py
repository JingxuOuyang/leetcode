class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        abfirst = x >= y
        cnt1, cnt2 = 0, 0
        for c in s:
            if c == 'a':
                if abfirst:
                    cnt2 += 1
                else:
                    if cnt2 > 0:
                        cnt2 -= 1
                        ans += y
                    else:
                        cnt1 += 1
            elif c == 'b':
                if abfirst:
                    if cnt2 > 0:
                        cnt2 -= 1
                        ans += x
                    else:
                        cnt1 += 1
                else:
                    cnt2 += 1
            else:
                if abfirst:
                    ans += min(cnt1, cnt2) * y
                else:
                    ans += min(cnt1, cnt2) * x
                cnt1 = cnt2 = 0
        if abfirst:
            ans += min(cnt1, cnt2) * y
        else:
            ans += min(cnt1, cnt2) * x
        return ans

s = Solution()
print(s.maximumGain("cdbcbbaaabab", 4, 5)) #20