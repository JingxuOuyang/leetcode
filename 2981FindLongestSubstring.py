
class Solution:
    def maximumLength(self, s: str) -> int:
        i = 0
        n = len(s)
        arr = []
        for j in range(26):
            arr.append([0] * 2)
        ans = -1
        while i < n:
            start = i
            ordc = ord(s[i]) - ord('a')
            i += 1
            while i < n:
               if (ord(s[i]) - ord('a') != ordc):
                   break
               i += 1
            k = i - start
            k2, count = arr[ordc][0], arr[ordc][1]
            if k2 == 0:
                arr[ordc][0] = k
                arr[ordc][1] = 1
                if k > 2:
                    t = k - 2
                    if t > ans:
                        ans = t
            else:
                if k2 < k:
                    arr[ordc][0] = k
                    arr[ordc][1] = 1
                    t = max(k2, k - 2)
                    if t > ans:
                        ans = t
                elif k2 == k:
                    arr[ordc][1] += 1
                    if arr[ordc][1] >= 3:
                        if k > ans:
                            ans = k
                    elif k > 1:
                        if k - 1 > ans:
                            ans = k - 1
                else:
                    if k > ans:
                        ans = k
        return ans

if __name__ == "__main__":
    slt = Solution()
    print(slt.maximumLength(s = "aaaa"))
    print(slt.maximumLength(s = "abcdef"))
    print(slt.maximumLength("abcaba"))
    print(slt.maximumLength("aabaaaaac"))