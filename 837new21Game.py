class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1
        dp = [0]*maxPts
        _p = 1 / maxPts
        dp[-1] = 1
        dpSum = 1
        s = 0
        for i in range(1, n + 1):
            idx = (i - 1) % maxPts
            p = dpSum * _p
            if i - maxPts < k:
                dpSum -= dp[idx]
            if i < k:
                dpSum += p
            else:
                s += p
                print(s)
            dp[idx] = p
        return s
    
s = Solution()
print(s.new21Game(n =12,k =1,maxPts =10))