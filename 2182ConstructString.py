from typing import List

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = list([0] * 26)
        for c in s:
            counts[ord(c) - ord('a')] += 1
        ans = list()
        i, j = 25, 24
        lastChar, t = -1, 0
        while i >= 0:
            if counts[i] == 0:
                i -= 1
            else:
                if lastChar == i:
                    if t < repeatLimit:
                        ans.append(chr(i + ord('a')))
                        t += 1
                        counts[i] -= 1
                    else:
                        while j >= i or (j >= 0 and counts[j] == 0):
                            j -= 1
                        if j < 0:
                            break
                        ans.append(chr(j + ord('a')))
                        counts[j] -= 1
                        lastChar = j
                        t = 1
                else:
                    ans.append(chr(i + ord('a')))
                    counts[i] -= 1
                    t = 1
                    lastChar = i
        return ''.join(ans)

if __name__ == '__main__':
    s = Solution()
    print(s.repeatLimitedString(s = "cczazcc", repeatLimit = 3))
    print(s.repeatLimitedString(s = "aababab", repeatLimit = 2))