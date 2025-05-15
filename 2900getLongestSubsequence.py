from typing import List
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        last = -1
        n = len(groups)
        for i in range(n):
            if last == groups[i]:
                continue
            ans.append(words[i])
            last = groups[i]
        return ans