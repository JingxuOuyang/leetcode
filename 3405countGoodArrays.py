MOD = 10 ** 9 + 7

def quickPower(base:int, power:int) -> int:
    ret = 1
    while power > 0:
        if power % 2 == 1:
            ret = (ret * base) % MOD
        base = (base * base) % MOD
        power >>= 1
    return ret

def compositeNumber(m: int, n:int)->int:
    m = min(m, n - m)
    ret = n - m + 1
    for i in range(m - 1):
        ret = (ret * (n - m + 2 + i) // (i + 2)) % MOD
    return ret

def combination_mod(n, k, mod = MOD):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    # 计算分子：n*(n-1)*...*(n-k+1) mod mod
    numerator = 1
    for i in range(k):
        numerator = numerator * (n - i) % mod
    
    # 计算分母：k! mod mod
    denominator = 1
    for i in range(1, k + 1):
        denominator = denominator * i % mod
    
    # 计算分母的逆元
    denominator_inv = pow(denominator, mod - 2, mod)
    
    # 计算组合数模值
    return numerator * denominator_inv % mod

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        ans = m
        ans = (ans * quickPower(m - 1, n - k - 1)) % MOD
        if k > 0:
            ans = (ans * combination_mod(n - 1, k)) % MOD
        return ans


print(combination_mod(4999, 20))
#print(compositeNumber(4, 10))
s = Solution()
# print(s.countGoodArrays(n = 3, m = 2, k = 1)) # 4
# print(s.countGoodArrays(n = 4, m = 2, k = 2)) # 6
# print(s.countGoodArrays(n = 5, m = 2, k = 0)) # 2
print(s.countGoodArrays(5000, 9999, 20)) # 226570611