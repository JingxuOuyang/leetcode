from typing import List

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        rightCounts = [0, 0, 0]
        n = len(s)
        for i in range(n-1, -1, -1):
            rightCounts[ord(s[i]) - ord('a')] += 1
        if any(x < k for x in rightCounts):
            return -1
        leftCounts = [0, 0, 0]
        i, j = -1, 0
        ans = n
        while i < ans - 1:
            if any(x + y < k for x, y in zip(leftCounts, rightCounts)):
                i += 1
                leftCounts[ord(s[i]) - ord('a')] += 1
                if j < n:
                    rightCounts[ord(s[j]) - ord('a')] -= 1
                    j += 1
                continue
            bFound = False
            while j < n:
                t = ord(s[j]) - ord('a')
                if leftCounts[t] + rightCounts[t] == k:
                    ans = i + 1 + n - j
                    i += 1
                    leftCounts[ord(s[i]) - ord('a')] += 1
                    rightCounts[ord(s[j]) - ord('a')] -= 1
                    j += 1
                    if j < n:
                        rightCounts[ord(s[j]) - ord('a')] -= 1
                        j += 1
                    bFound = True
                    break
                rightCounts[t] -= 1
                j += 1
            if not bFound:
                ans = i + 1
                i += 1
        return ans
            
            
    
if __name__ == "__main__":
    s = Solution()
    print(s.takeCharacters(s = "aabaaaacaabc", k = 2))
    print(s.takeCharacters('a', 1))
    print(s.takeCharacters('bcca', 1))
    