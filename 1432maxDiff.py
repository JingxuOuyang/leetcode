class Solution:
    def maxDiff(self, num: int) -> int:
        digits = []
        t = num
        while t > 0:
            digits.append(t % 10)
            t //= 10
        n = len(digits)
        if digits[-1] == 9:
            ans = 0
            i = n - 1
            while i >= 0 and digits[i] == 9:
                ans = ans * 10 + 8
                i -= 1
            if i < 0:
                return ans
            a = digits[i]
            while i >= 0:
                if digits[i] == a:
                    ans = ans * 10 + 9 - a
                elif digits[i] == 9:
                    ans = ans * 10 + 8
                else:
                    ans *= 10
                i -= 1
            return ans
        elif digits[-1] == 1:
            ans = 0
            i = n - 1
            while i >= 0 and (digits[i] == 1 or digits[i] == 0):
                if digits[i] == 1:
                    ans = ans * 10 + 8
                else:
                    ans *= 10
                i -= 1
            if i < 0:
                return ans
            a = digits[i]
            while i >= 0:
                if digits[i] == a:
                    ans = ans * 10 + a
                elif digits[i] == 1:
                    ans = ans * 10 + 8
                else:
                    ans *= 10
                i -= 1
            return ans
        else:
            ans = 0
            for i in range(n - 1, -1, -1):
                if digits[i] == digits[-1]:
                    ans = ans * 10 + 8
                else:
                    ans *= 10
            return ans

s = Solution()
#print(s.maxDiff(123456))
print(s.maxDiff(1101057)) # 8808050