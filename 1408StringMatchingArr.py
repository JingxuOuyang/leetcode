from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x : len(x))
        n = len(words)
        ans = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                if words[j].find(words[i]) != -1:
                    ans.append(words[i])
                    break
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.stringMatching(words =["leetcoder","leetcode","od","hamlet","am"]))