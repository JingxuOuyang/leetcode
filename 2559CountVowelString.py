from typing import List

vowels = ['a', 'o', 'e', 'u', 'i']
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        m = len(words)
        counts = [0] * (m + 1)
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                counts[i + 1] = counts[i] + 1
            else:
                counts[i + 1] = counts[i]
        ans = [0] * n
        for i, query in enumerate(queries):
            ans[i] = counts[query[1] + 1] - counts[query[0]]
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))
    print(s.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]))