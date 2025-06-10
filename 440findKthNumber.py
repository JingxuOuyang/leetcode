class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        digits = []
        m = n
        while m > 0:
            digits.append(m % 10)
            m //= 10
        mod = 1
        for i in range(len(digits) - 1):
            mod = 1 + 10*mod
        ans = 0
        def kseqNum(k:int, mod:int, ans:int) -> int:
            if k == 0:
                return ans
            k -= 1
            ans = ans * 10 + (k // mod)
            k %= mod
            mod //= 10
            return kseqNum(k, mod, ans)

        def func(digit_index:int, k:int, mod:int, vol:int, ans:int)->int:
            if k == 0:
                return ans
            k -= 1
            vol -= 1
            a = digits[digit_index]
            head = a * mod
            tail = (9 - a) * (mod // 10)
            mid = vol - head - tail
            if k <= head:
                ans = ans * 10 + (k // mod)
                return kseqNum(k % mod, mod // 10, ans)
            else:
                k -= head
                if k <= mid:
                    ans = ans * 10 + a
                    return func(digit_index - 1, k, mod//10, mid, ans)
                else:
                    k -= mid
                    mod //= 10
                    ans = ans * 10 + (k // mod) + a + 1
                    return kseqNum(k % mod, mod // 10, ans)
        head = (digits[-1] - 1) * mod
        tail = (9 - digits[-1]) * (mod // 10)
        mid = n - head - tail
        k -= 1
        if k < head:
            ans = (k // mod) + 1
            return kseqNum(k % mod, mod // 10, ans)
        else:
            k -= head
            if k < mid:
                ans = digits[-1]
                return func(-2, k, mod//10, mid, ans)
            else:
                k -= mid
                mod //= 10
                ans = digits[-1] + 1 + k // mod
                k %= mod
                return kseqNum(k, mod // 10, ans)

s = Solution()
print(s.findKthNumber(13,2))
print(s.findKthNumber(13, 5))
print(s.findKthNumber(13, 1))
print(s.findKthNumber(13, 10))