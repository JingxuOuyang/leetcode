from typing import List

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n, m = len(str1), len(str2)
        j = 0
        for i in range(n):
            if j == m:
                break
            vi, vj = ord(str1[i]), ord(str2[j])
            if vi == vj or vi + 1 == vj or (vi == ord('z') and vj == ord('a')):
                j += 1
        return j == m

if __name__ == "__main__":
    s = Solution()
    print(s.canMakeSubsequence(str1 = "abc", str2 = "ad"))
    print(s.canMakeSubsequence(str1 = "zc", str2 = "ad"))
    print(s.canMakeSubsequence(str1 = "ab", str2 = "d"))