from typing import List
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        mask = (1 << (n - 1))
        totalNum = 3 * mask
        if k > totalNum:
            return ""
        idx = k - 1
        
        ans = [idx // mask]
        idx = idx % mask
        mask >>= 1
        while mask > 0:
            p = idx // mask
            if p >= ans[-1]:
                p += 1
            ans.append(p)
            idx %= mask
            mask >>= 1
        ans = [chr(ord('a') + p) for p in ans]
        return ''.join(ans)

s = Solution()
#print(s.getHappyString(n = 1, k = 3))
print(s.getHappyString(n = 3, k = 9))