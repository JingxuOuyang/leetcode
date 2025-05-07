MOD = 10 ** 9 + 7
class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        f, f2, g = 2, 1, 1
        for i in range(3, n + 1):
            next_f = (f + 2 * g + f2) % MOD
            next_g = (f2 + g) % MOD
            f2 = f
            f = next_f
            g = next_g
        return f 
    
s = Solution()
print(s.numTilings(3))