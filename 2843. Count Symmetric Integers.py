dparr = [0, 63, 132, 205, 280, 355, 428, 497, 560, 615]
def countNum(num:int)->int:
    if num == 10000:
        return 615
    if num < 10:
        return 0
    bits = []
    while num > 0:
        bits.append(num % 10)
        num //= 10
    if len(bits) == 3:
        return 9
    if len(bits) == 2:
        return bits[1] if bits[1] <= bits[0] else bits[1] - 1
    # 4位
    ans = dparr[bits[-1] - 1]
    t = bits[-1] + bits[-2]
    if t < 10:
        ans += (bits[-1] + t + 1) * bits[-2] // 2
        t2 = bits[0] + bits[1]
        if bits[1] > t:
            ans += t + 1
        else:
            if t2 >= t:
                ans += bits[1] + 1
            else:
                ans += bits[1]
    else:
        ans += (11 + bits[-1]) * (10 - bits[-1]) // 2
        ans += (29 - t) * (t - 10) // 2
        if bits[1] >= t - 9:
            t2 = bits[0] + bits[1]
            if t2 >= t:
                ans += bits[1] + 10 - t
            else:
                ans += bits[1] + 9 - t
    return ans + 9


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        return countNum(high) - countNum(low - 1)

s = Solution()
#print(s.countSymmetricIntegers(low = 1, high = 100))
print(s.countSymmetricIntegers(low = 1, high = 3899)) #353
# print(s.countSymmetricIntegers(1, 3029)) # 419