class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        lenOfSuffix = len(s)
        suffixMask = 10 ** lenOfSuffix
        sNumber = int(s)
        flagA, flagB = (finish % suffixMask) >= sNumber, (start % suffixMask) <= sNumber
        dpA, dpB = 1 if flagA else 0, 1 if flagB else 0
        finish //= suffixMask
        start //= suffixMask
        t = 1 # (limit + 1) ** k
        while start // 10 != finish // 10:
            ai, bi = finish % 10, start % 10
            if ai > limit:
                dpA = t * (limit + 1)
            else:
                dpA += ai * t
            
            if bi > limit:
                dpB = 0
            else:
                dpB += (limit - bi) * t
            start //= 10
            finish //= 10
            t *= (limit + 1)

        ai, bi = finish % 10, start % 10
        if bi <= limit:
            ans = dpB
        else:
            ans = 0
        ans += (min(limit, ai - 1) - bi) * t
        if ai <= limit:
            ans += dpA
        return ans

s = Solution()
print(s.numberOfPowerfulInt(start = 3, finish = 1429, limit = 5, s = "34"))
print(s.numberOfPowerfulInt(start = 1, finish = 6000, limit = 4, s = "124"))
print(s.numberOfPowerfulInt(start = 15, finish = 215, limit = 6, s = "10"))
print(s.numberOfPowerfulInt(start = 1000, finish = 2000, limit = 4, s = "3000"))
        


            