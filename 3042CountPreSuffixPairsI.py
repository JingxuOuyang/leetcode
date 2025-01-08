from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        #words.sort(key=lambda w : len(w))
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    ans+=1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.countPrefixSuffixPairs(words = ["a","aba","ababa","aa"]))
    print(s.countPrefixSuffixPairs(words = ["pa","papa","ma","mama"]))